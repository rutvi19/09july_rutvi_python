from django.urls import path,include
from userapp import views  

urlpatterns = [
   path('',views.index),  
    path('login/',views.login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('otp/',views.otp,name='otp'),
    path('userlogout/',views.userlogout,name='userlogout'),
    path('profile/',views.profile,name='profile'),
]