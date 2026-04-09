from integration.router import process_request
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def api_gateway(request, path=""):
    body = None
    if request.method == "POST":
        body = json.loads(request.body)
    response = process_request(path, body, request.method)
    return JsonResponse(response, safe=False)  # <- safe=False for lists
"""
def create_report(request):
    method = request.method
    body = None
    if method == "POST":
        import json
        body = json.loads(request.body)


    # tell integration manager which system + action
    path = "reporting/report"
    data = process_request(path, body, method)
    return JsonResponse(data)

@csrf_exempt
def api_gateway(request, path=""):
    if request.method not in ["GET", "POST"]:
        return JsonResponse({"error": "Method not allowed"}, status=405)

    try:
        body = json.loads(request.body) if request.body else {}
    except:
        return JsonResponse({"error": "Invalid JSON"}, status=400)

    response = process_request(path, body, request.method)
    return JsonResponse(response)

from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


# (Temporary routing - will move to integrator Day 7)
def route_request(path, body):

    parts = path.split("/")

    if len(parts) < 2:
        return {"error": "Invalid route format"}

    system = parts[0]
    action = parts[1]

    # TEMP simulation (Day 6 only)
    return {
        "system": system,
        "action": action,
        "message": f"{action} executed on {system}",
        "data": body
    }


@csrf_exempt
def api_gateway(request, path=""):

    # METHOD VALIDATION
   
    if request.method not in ["GET", "POST"]:
        return JsonResponse({"error": "Method not allowed"}, status=405)

    
    if request.method == "POST" and request.content_type != "application/json":
        return JsonResponse({"error": "Only JSON allowed"}, status=400)

    #  JSON PARSING
  
    try:
        body = json.loads(request.body) if request.body else {}
    except:
        return JsonResponse({"error": "Invalid JSON"}, status=400)

   
    # 4. ROUTING (TEMP)
    
    response = route_request(path, body)

    return JsonResponse(response)"""







