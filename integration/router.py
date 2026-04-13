from connectors import sysA
from django.urls import path
from . import views

urlpatterns = [
    path("create", views.create_report, name="create_report"),
]
def process_request(path, body, method):
    parts = path.split("/")
    system = parts[0] if len(parts) > 0 else None
    action = parts[1] if len(parts) > 1 else None

    print("DEBUG:", system, action)
    if system == "reports":
        return sysA.handle(system,action, body, method)
    elif system == "interns":
        return sysA.handle(system, action, body, method)
    else:
        return {"error": "Unknown system"}



"""

    if system == "reports":
        if method == "GET":
            return {"message": "GET reports working"}

        elif method == "POST":
            return {"message": "POST reports working"}

    return {"error": "Invalid route"}
from connectors.restconnect import handle_rest

def route_request(request):
    # simple logic for now
    if request.path.startswith('/api/test'):
        return handle_rest(request)
    
    return {"error": "No route found"}"""
    