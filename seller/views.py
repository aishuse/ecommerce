from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView, ListView

from seller.forms import ProductAddForm, ProductStockForm
from seller.models import Product, ProductStock


class ProductAdd(CreateView):
    model = Product
    template_name = 'seller/product_create.html'
    form_class = ProductAddForm
    success_url = 'stockadd'
    context_object_name = 'products'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ProductAdd, self).form_valid(form)


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


class MyProducts(ListView):
    model = Product
    template_name = 'seller/my_products.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.filter(user=self.request.user)