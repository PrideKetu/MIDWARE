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

from connectors.ExpressConnect import forward_report_to_express

def route_request(target_system, data):
    cleaned = str(target_system).strip().lower()

    if cleaned == "express":
        
        return forward_report_to_express(data)

    print("NO MATCH")
    return {
        "status": "error",
        "message": f"Unknown target system: {cleaned}"
    }