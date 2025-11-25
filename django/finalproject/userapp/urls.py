from django.urls import path,include
from userapp import views  

urlpatterns = [
   path('',views.index),  
    path('login/',views.login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('otp/',views.otp,name='otp'),
]
