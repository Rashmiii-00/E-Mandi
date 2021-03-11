from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('Home', views.loadHomePage),
    path('vegetables', views.loadVegetables),
    path('fruits', views.loadFruits),
    path('cereals', views.loadCereals),
    path('addToCart', views.add),
    path('bookPage', views.bookpage),
    path('confirm', views.confirm)
]