
from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.views.generic import (CreateView, TemplateView)
from authapp.forms import SellerSignUpForm, CustomerSignUpForm
from authapp.models import User


class MultiSignup(TemplateView):
    template_name = 'authapp/account.html'


class Home(TemplateView):
    template_name = 'authapp/base.html'

class Sellerhome(TemplateView):
    template_name = "authapp/sellerhome.html"

class SellerSignUpView(CreateView):
    model = User
    form_class = SellerSignUpForm
    template_name = 'authapp/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'seller'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('myproducts')

class CustomerSignUpView(CreateView):
    model = User
    form_class = CustomerSignUpForm
    template_name = 'authapp/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'customer'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('products')


def home(request):
    if request.user.is_authenticated:
        if request.user.is_seller:
            return redirect('myproducts')
        else:
            return redirect('products')
    return render(request, 'authapp/base.html')