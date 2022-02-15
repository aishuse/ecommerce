from django.urls import path, include
from authapp import views

urlpatterns = [

    path('multisignup', views.MultiSignup.as_view(), name='multisignup'),
    path('sellerhome', views.Sellerhome.as_view(), name='sellerhome')

]