import stripe as stripe
from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

from customer.models import Cart, Purchase
from ecommerce import settings
stripe.api_key = settings.STRIPE_SECRET_KEY


class GatewayView(TemplateView):
    template_name = "stripe/stripe.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart_products = Cart.objects.filter(user=self.request.user, status='incart')
        total = 0
        for cart in cart_products:
            total += cart.item.price * cart.quantity
        context['total'] = total
        context['amount'] = total * 100
        print("total=", total)
        context['key'] = settings.STRIPE_PUBLISHABLE_KEY
        return context


def charge(request, amount=None, *args, **kwargs):
    cart_products = Cart.objects.filter(user=request.user, status='incart')
    total = 0
    for cart in cart_products:
        total += cart.item.price * cart.quantity
    if request.method == "POST":
        payment_intent = stripe.PaymentIntent.create(
            amount=total*100,
            currency="INR",
            description="book purchase",
            payment_method_types=["card"],
        )
        cart_item = Cart.objects.filter(user=request.user, status='incart')
        buy = Purchase.objects.filter(status="pending", user=request.user)
        for i in cart_item:
            i.status = 'cancelled'
            i.item.stock = i.item.stock - i.quantity
            i.item.save()
            i.save()
        for i in buy:
            i.status = 'orderplaced'
            i.save()
        return render(request, 'stripe/payment.html', payment_intent)
    return render(request, 'stripe/payment.html')
