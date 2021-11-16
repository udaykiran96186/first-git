from app1 import views
from django.urls import path

 
urlpatterns = [
    path('', views.home, name='home'),
    path('hello', views.hello, name='hello'),
    path('joker', views.joker, name='joker'),
]