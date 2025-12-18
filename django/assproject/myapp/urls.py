from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('clien_register',views.client_register,name='client_register'),
]    