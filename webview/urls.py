from django.urls import path, include
from . import views
urlpatterns = [
   path('', views.home, name="home"),
   path('users', views.pvrusers, name='pvrusers'),
   path('adminusers', views.addNewAdmin, name='adminusers'),
   path('singlemail', views.sendSingleMail, name='singlemail'),
   path('multipleemail', views.sendMovieNotification, name='multipleemail'),
   path('movie', views.movie, name='movie')
]
