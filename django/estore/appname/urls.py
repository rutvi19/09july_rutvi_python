from django.contrib import admin
from django.urls import path,include
from appname import views

urlpatterns = [
   path('',views.home),
   path('signup/',views.signup),
   path('login/',views.login),
]