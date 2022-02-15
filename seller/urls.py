from django.urls import path
from seller import views

urlpatterns = [
    path('productadd', views.ProductAdd.as_view(), name='productadd'),
    path('stockadd', views.StockAdd.as_view(),name='stockadd'),
    path('myproducts', views.MyProducts.as_view(), name='myproducts'),



]