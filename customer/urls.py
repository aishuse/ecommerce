from django.urls import path
from customer import views

urlpatterns = [
    path('home/', views.CustHome.as_view(), name='custindex'),
    path('products', views.Products.as_view(), name='products'),

    path('productdetail/<int:pk>', views.ProductDetails.as_view(), name='productdetails'),
    path('addtocart/<int:pk>', views.AddToCart.as_view(), name='addtocart'),
    path('mycart', views.ViewMyCart.as_view(), name='mycart'),
    path('cart/plus/<int:pk>', views.cart_plus, name='plus'),
    path('cart/minus/<int:pk>', views.cart_minus, name='minus'),
    path('carts/item/remove/<int:pk>', views.RemoveFromCart.as_view(), name='removeitem'),
    path("checkout", views.CheckoutView, name="checkout"),
    path('order/<int:pk>', views.placeorder, name='placeorder'),

    path("myorders", views.MyOrders.as_view(), name='viewmyorder'),

    path('categorylist', views.ListCategory.as_view(), name='categorylist'),

    path('categorydetail/<int:pk>', views.Categories.as_view(), name='catdetail'),

]
