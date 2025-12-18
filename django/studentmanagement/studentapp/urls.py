from django.urls import path
from studentapp import views

urlpatterns = [
    path('',views.index,name='index'),
    path('stddashboard/',views.stddashboard,name='stddashboard'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('userlogout/',views.userlogout,name='userlogout'),
]
