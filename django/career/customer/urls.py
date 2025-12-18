from django.contrib import admin
from django.urls import path
from customer import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('login/',views.login,name='login'),
    path('cancel_booking/',views.cancel_booking,name='cancel_booking'),
    path('book_artist/',views.book_artist,name='book_artist'),
    path('feedback/',views.feedback,name='feedback'),
    path('manage_booking/',views.manage_booking,name='manage_booking'),
    path('manage_profile/',views.manage_profile,name='manage_profile'),
    path('register/',views.register,name='register'),
    path('search_artist/',views.search_artist,name='search_artist'),

]