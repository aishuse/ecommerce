
from django.urls import path, include
from api import views
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import routers

# router = routers.SimpleRouter()
# router.register(r'events', views.EventModelViewset, basename="events")

urlpatterns = [


    path("products/", views.ProductMixin.as_view()),

    path('accounts/register/', views.Registration.as_view()),
    path('accounts/signin/', views.Login.as_view()),
    path('accounts/signout/', views.Logout.as_view()),

]