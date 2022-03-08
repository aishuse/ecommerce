from django.urls import path
from sendemail import views

urlpatterns = [
    path('sendmail/', views.SendEmail.as_view(), name="sendmail"),
    path('', views.test, name='test'),

]