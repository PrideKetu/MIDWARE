from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_entry),
    path('health/', views.health),
]