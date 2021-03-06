"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from authapp import views

# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )

urlpatterns = [
                  path('', views.home, name='home'),
                  path('admin/', admin.site.urls),
                  path('authapp/', include('authapp.urls')),
                  path('seller/', include('seller.urls')),
                  path('customer/', include('customer.urls')),
                  path('stripeapp/', include('stripeapp.urls')),
                  path('celery/', include('sendemail.urls')),

                  path('admins/', include('admins.urls')),
                  # path('api/', include('api.urls')),
                  path('accounts/', include('django.contrib.auth.urls')),
                  path('accounts/signup/seller/', views.SellerSignUpView.as_view(), name='sellersignup'),
                  path('accounts/signup/customer/', views.CustomerSignUpView.as_view(), name='customersignup'),
                  re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
                  re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
                  # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
                  # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
