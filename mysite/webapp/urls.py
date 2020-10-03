from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
	path('getprice', views.getPrice, name='getprice'),
	path('todelete', views.toDelete, name='todelete'),
]
