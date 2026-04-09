from django.urls import path
from . import views

from django.urls import path
from .views import api_gateway

urlpatterns = [
    
    path('<path:path>/', api_gateway),
    path('', api_gateway),  # root
]
