from django.urls import path

from stripeapp import views

urlpatterns = [
    path("order/proceed", views.GatewayView.as_view(), name="payment-gateway"),
    path("order/payment", views.charge, name="payment"),


]