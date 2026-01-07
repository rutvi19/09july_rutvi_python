from django.urls import path
from studentapp import views

urlpatterns = [
    path('',views.index,name='index'),
    path('stddashboard/',views.stddashboard,name='stddashboard'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('userlogout/',views.userlogout,name='userlogout'),
    path('profile/',views.profile,name='profile'),
    path('course/',views.course,name='course'),
    path('otpverify/',views.otpverify,name='otpverify'),
    path('contact/',views.contact,name='contact'),
    path('notes/',views.notes,name='notes'),
    path('aboutus/',views.aboutus,name='aboutus'),  
]

