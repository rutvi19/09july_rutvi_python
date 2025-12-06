from django.contrib import admin
from django.urls import path
from customer import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home.html'),
    path('login/',views.login,name='login.html'),
    path('cancel_booking/',views.cancel_booking,name='cancel_booking.html'),
    path('book_artist/',views.book_artist,name='book_artist.html'),
    path('feedback/',views.feedback,name='feedback.html'),
    path('manage_booking/',views.manage_booking,name='manage_booking.html'),
    path('manage_profile/',views.manage_profile,name='manage_profile.html'),
    path('register/',views.register,name='register.html'),
    path('search_artist/',views.search_artist,name='search_artist.html'),

]