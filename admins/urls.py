from django.urls import path
from admins import views

urlpatterns = [
    path('admin/home', views.AdminHome.as_view(), name='adminhome'),
    path('categoryadd', views.CategoryCreate.as_view(), name='addcategory'),
    path('categorylist', views.CategoryList.as_view(), name='listcategory')
    ]