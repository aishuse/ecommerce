from django.urls import path
from seller import views

urlpatterns = [
    path('productadd', views.ProductAdd.as_view(), name='productadd'),
    path('stockadd', views.StockAdd.as_view(), name='stockadd'),
    path('myproducts', views.MyProducts.as_view(), name='myproducts'),
    path('product/details/<int:pk>', views.ProductDetails.as_view(), name='proddetails'),
    path('bookupdate/<int:pk>', views.ProductUpdate.as_view(), name='productupdate'),
    path('bookdelete/<int:pk>', views.ProductDelete.as_view(), name='productdelete'),
    path('stockavailable', views.StockView.as_view(), name='stockavailable'),
    path('outofstock', views.OutofStock.as_view(), name='outofstock'),
    path("orders/list", views.ViewOrders.as_view(), name='customerorders'),
    path('orders/change/<int:pk>', views.OrderUpdateView.as_view(), name='orderchange'),
    path("orders/view/<int:pk>", views.ViewSingleCustomer.as_view(), name="cust_single_order"),

]
