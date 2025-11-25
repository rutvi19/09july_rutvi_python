from django.urls import path
from doctorapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_doctor/', views.add_doctor, name='add_doctor'), 
    path('doctor_list', views.doctor_list, name='doctor_list'),
    path('register/', views.register_patient, name='register'),
]
