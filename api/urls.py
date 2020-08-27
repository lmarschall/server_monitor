  
from django.urls import path

from . import views

urlpatterns = [
    path('cpu_count', views.cpu_count, name='cpu_count')
]