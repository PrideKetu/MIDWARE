from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse

def create_report(request):
    return JsonResponse({"status": "ok", "message": "Report endpoint works"})