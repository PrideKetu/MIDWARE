from django.urls import path
from . import views

from django.urls import path
from .views import api_gateway
from .views import test_express

urlpatterns = [
    path("send/<str:system>/", test_express),
    path('<path:path>/', api_gateway),
    path('', api_gateway),  # root
   
    
]
