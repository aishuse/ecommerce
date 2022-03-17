from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView, TemplateView

from authapp.decorators import seller_required
from customer.models import Purchase
from seller.forms import ProductAddForm, ProductStockForm, OrderUpdateForm
from seller.models import Product, ProductStock


@method_decorator([login_required, seller_required], name='dispatch')
class ProductAdd(CreateView):
    model = Product
    template_name = 'seller/product_create.html'
    form_class = ProductAddForm
    success_url = 'stockadd'
    context_object_name = 'products'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ProductAdd, self).form_valid(form)


@method_decorator([login_required, seller_required], name='dispatch')
class StockAdd(CreateView):
    model = ProductStock
    template_name = 'seller/stock.html'
    form_class = ProductStockForm
    success_url = 'myproducts'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.instance.user = self.request.user
        product = Product.objects.get(id=form.data.__getitem__('product'))
        stockavailable = form.data.__getitem__('stock_available')
        product.stock = product.stock + int(stockavailable)
        product.save()
        return super(StockAdd, self).form_valid(form)


@method_decorator([login_required, seller_required], name='dispatch')
class MyProducts(ListView):
    model = Product
    template_name = 'seller/my_products.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.filter(user=self.request.user)


@method_decorator([login_required, seller_required], name='dispatch')
class ProductDetails(DetailView):
    model = Product
    template_name = 'seller/product_detail.html'
    context_object_name = 'products'


@method_decorator([login_required, seller_required], name='dispatch')
class ProductUpdate(UpdateView):
    model = Product
    template_name = 'seller/product_update.html'
    form_class = ProductAddForm
    success_url = '/seller/myproducts'


@method_decorator([login_required, seller_required], name='dispatch')
class ProductDelete(DeleteView):
    model = Product
    template_name = 'seller/delete.html'
    success_url = '/seller/myproducts'


@method_decorator([login_required, seller_required], name='dispatch')
class OutofStock(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'seller/outofstock.html'

    def get_queryset(self):
        return Product.objects.filter(user=self.request.user, stock=0)


@method_decorator([login_required, seller_required], name='dispatch')
class StockView(ListView):
    model = ProductStock
    template_name = 'seller/stock_history.html'
    context_object_name = 'stocks'

    def get_queryset(self):
        return ProductStock.objects.filter(user=self.request.user)


@method_decorator([login_required, seller_required], name='dispatch')
class ViewOrders(TemplateView):
    model = Purchase
    template_name = "seller/orders.html"

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        count = self.model.objects.filter(status='orderplaced', seller=self.request.user).count()
        context['order_count'] = count
        context['orders'] = self.model.objects.filter(status='orderplaced', seller=self.request.user)

        dispatch = self.model.objects.filter(status='dispatch', seller=self.request.user)
        context['dispatch'] = dispatch
        context['dispatch_count'] = dispatch.count()

        intransit = self.model.objects.filter(status='intransit', seller=self.request.user)
        context['intransit'] = intransit
        context['intransit_count'] = intransit.count()

        delivered = self.model.objects.filter(status='delivered', seller=self.request.user)
        context['delivered'] = delivered
        context['delivered_count'] = delivered.count()

        ordercancelled = self.model.objects.filter(status='ordercancelled', seller=self.request.user)
        context['ordercancelled'] = ordercancelled
        context['ordercancelled_count'] = ordercancelled.count()
        return context


@method_decorator([login_required, seller_required], name='dispatch')
class ViewSingleCustomer(DetailView):
    model = Purchase
    template_name = "seller/customer_order_detail.html"
    context_object_name = "order"


@method_decorator([login_required, seller_required], name='dispatch')
class OrderUpdateView(UpdateView):
    model = Purchase
    template_name = 'seller/orderupdate.html'
    form_class = OrderUpdateForm
    success_url = reverse_lazy("customerorders")



