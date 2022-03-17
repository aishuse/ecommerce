from datetime import datetime, timedelta

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator

from django.views.generic import TemplateView, ListView, DetailView

from admins.models import Category
from authapp.decorators import customer_required
from customer.models import Cart, Address, Purchase
from ecommerce import settings
from seller.models import Product


@method_decorator([login_required, customer_required], name='dispatch')
class CustHome(TemplateView):
    template_name = 'customer/index.html'


@method_decorator([login_required, customer_required], name='dispatch')
class Products(ListView):
    model = Product
    template_name = 'customer/product_list.html'
    context_object_name = 'products'


@method_decorator([login_required, customer_required], name='dispatch')
class ProductDetails(DetailView):
    model = Product
    template_name = 'customer/product_detail.html'
    context_object_name = 'products'


@method_decorator([login_required, customer_required], name='dispatch')
class AddToCart(TemplateView):
    model = Cart

    def get(self, request, *args, **kwargs):
        pk = kwargs['pk']
        product = Product.objects.get(pk=pk)
        if Cart.objects.filter(item=product, user=self.request.user, status='incart').exists():
            pass

        else:
            cart = Cart.objects.create(item=product, user=self.request.user)
            cart.save()
            print('product added')
        return redirect('products')


def cart_plus(request, *args, **kwargs):
    id = kwargs['pk']
    cart = Cart.objects.get(id=id)
    cart.quantity += 1
    cart.save()
    return redirect('mycart')


def cart_minus(request, *args, **kwargs):
    id = kwargs['pk']
    cart = Cart.objects.get(id=id)
    cart.quantity -= 1
    cart.save()
    if cart.quantity < 1:
        return redirect('removeitem', cart.id)
    return redirect('mycart')


@method_decorator([login_required, customer_required], name='dispatch')
class ViewMyCart(TemplateView):
    model = Cart
    template_name = 'customer/mycart.html'
    context = {}

    def get(self, request, *args, **kwargs):
        mycart = self.model.objects.filter(user=self.request.user, status='incart')
        total = 0
        for cart in mycart:
            if cart.quantity > cart.item.stock:
                cart.quantity = cart.item.stock
                cart.save()
            if (cart.quantity == 0) & (cart.item.stock != 0):
                cart.quantity = 1
                cart.save()
            total += cart.item.price * cart.quantity

        self.context['items'] = mycart
        self.context['total'] = total
        return render(request, self.template_name, self.context)


@method_decorator([login_required, customer_required], name='dispatch')
class RemoveFromCart(TemplateView):
    model = Cart

    def get(self, request, *args, **kwargs):
        pk = kwargs['pk']
        cart = self.model.objects.get(pk=pk)
        cart.status = 'cancelled'
        cart.save()
        return redirect('mycart')


# @method_decorator([login_required, customer_required], name='dispatch')
@login_required()
def CheckoutView(request):
    address = Address.objects.filter(user=request.user)
    addr = []
    for i in address:
        data = {}
        data['name'] = i.name
        data['mob'] = i.mob_no
        data['address'] = '{}, {}, {}, {}, India, {} '.format(i.house, i.street, i.town, i.state, i.pin)
        data['landmark'] = '{}'.format(i.landmark)
        data['id'] = i.id
        addr.append(data)
    print('addresses :', addr)
    context = {
        'address': addr
    }
    if request.method == "POST":
        print(request.POST)
        x = request.POST
        new_address = Address()
        new_address.user = request.user
        new_address.name = x['name']
        new_address.mob_no = x['mob_no']
        new_address.house = x['house']
        new_address.street = x['street_address']
        new_address.town = x['town']
        new_address.state = x['state']
        new_address.pin = x['pin']
        new_address.landmark = x['landmark']
        if (Address.objects.filter(house=x['house'], pin=x['pin']).exists()):
            print('already exists')
        else:
            new_address.save()
            return redirect("checkout")
    return render(request, 'customer/checkout.html', context)



def placeorder(request, *args, **kwargs):
    cart_item = Cart.objects.filter(user=request.user, status='incart')
    address = Address.objects.get(id=kwargs.get('pk'))
    ad = '{},{},{}, {}, {}, {}, India, {} '.format(address.name, address.mob_no, address.house, address.street,
                                                   address.town, address.state, address.pin, address.landmark)
    for i in cart_item:
        if i.item.stock == 0:
            i.status = 'cancelled'
        else:
            order = Purchase()
            if (Purchase.objects.filter(item=Product.objects.get(id=i.item.id), user=request.user, address=ad,
                                       status='pending')).exists():
                print('already exists')
            else:
                order.item = Product.objects.get(id=i.item.id)
                order.user = request.user
                order.seller = Product.objects.get(id=i.item.id).user
                order.address = ad
                order.quantity = i.quantity
                order.price = (i.item.price) * (i.quantity)
                order.expected_delivery = datetime.now() + timedelta(days=7)
                order.status = 'pending'
                order.save()
    total = 0
    data = []
    for i in cart_item:
        context = {}
        item = Product.objects.get(id=i.item_id)
        context['image'] = item.image
        context['name'] = item.name
        context['quantity'] = i.quantity
        context['price'] = item.price
        context['address'] = ad
        total += i.item.price * i.quantity
        context['total'] = total
        data.append(context)
    return render(request, 'customer/order_summary.html', {'data': data, 'address': ad, 'total': total})


@method_decorator([login_required, customer_required], name='dispatch')
class MyOrders(ListView):
    model = Purchase
    template_name = 'customer/myorders.html'
    context_object_name = "orders"

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = self.model.objects.filter(user=self.request.user)
        return queryset


@method_decorator([login_required, customer_required], name='dispatch')
class ListCategory(ListView):
    model = Category
    template_name ='customer/categorylist.html'
    context_object_name = 'category'


@method_decorator([login_required, customer_required], name='dispatch')
class Categories(ListView):
    model = Category
    template_name = 'customer/categorydetail.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        obj = Category.objects.get(pk=self.kwargs['pk'])
        cat = obj.category.all()
        context['cat'] = cat
        context['obj'] = obj
        return context
