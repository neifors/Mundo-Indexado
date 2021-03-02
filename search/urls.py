from django.urls import path
from . import views

urlpatterns = [
    path('pccomponentes', views.pccomponentes, name='pccomponentes')
]