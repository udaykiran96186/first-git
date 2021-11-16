from app1 import views
from django.urls import path

 
urlpatterns = [
    path('', views.home, name='home'),
    path('hello', views.hello, name='hello'),
    path('joker', views.joker, name='joker'),
    path('getData', views.getData, name='getData'),
    path('getName', views.getName, name='getName'),
    path('get/<int:id>', views.get),
    path('formView', views.formView,name="formView"),
    path('formHtml', views.formHtml,name="formHtml"),

]