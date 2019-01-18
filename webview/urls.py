from django.urls import path, include
from . import views
urlpatterns = [
   path('', views.home, name="home"),
   path('users', views.pvrusers, name='pvrusers'),
   path('adminusers', views.addNewAdmin, name='adminusers'),
]
