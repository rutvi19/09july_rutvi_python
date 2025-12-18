from django.urls import path
from studentapp import views

urlpatterns = [
    path('login/',views.index,name='login'),
]
