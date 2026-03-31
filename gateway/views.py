from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from integration.router import route_request

def health(request):
    return JsonResponse({
        "status": "ok",
        "message": "Middleware is running"
    })

def api_entry(request):
    response = route_request(request)
    return JsonResponse(response)