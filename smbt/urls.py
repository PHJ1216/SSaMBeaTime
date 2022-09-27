from django.urls import path, include
from . import views

app_name = 'smbt'

urlpatterns = [
    path('', views.index),
]
