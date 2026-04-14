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

from integration.router import route_request
def test_express(request, system):
    print("🔥 VIEW SYSTEM:", system)
    data = {
        "title": "Middleware Report",
        "intern_id": 101,
        "description": "Testing Express integration"
    }

    result = route_request(system, data)

    return JsonResponse(result)