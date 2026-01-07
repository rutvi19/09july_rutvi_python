from django.urls import path
from facultyapp import views

urlpatterns = [
    path('fa_login/',views.fa_login,name='fa_login'),
    path('fa_register/',views.fa_register,name='fa_register'),
    path('fa_dashboard/',views.fa_dashboard,name='fa_dashboard'),
    path('delete_student/<int:id>/',views.delete_student,name='delete_student'),

]