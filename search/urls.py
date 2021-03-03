from django.urls import path
from . import views

urlpatterns = [
    path('super_search', views.super_search, name='super_search')
]