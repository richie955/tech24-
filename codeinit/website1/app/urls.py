
from django.urls import path,include
from app import views
urlpatterns = [
   path('', views.home, name='home'),
   path('signup', views.handle, name='handle'),
]
   
   
