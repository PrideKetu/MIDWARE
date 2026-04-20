# =========================
# ❌ OLD SYSTEM (KEEP BUT DISABLE)
# =========================

# from connectors.sysA import handle
# from django.urls import path
# from . import views
#
# urlpatterns = [
#     path("create", views.create_report, name="create_report"),
# ]
#
# def process_request(path, body, method):
#
#     parts = path.strip("/").split("/")
#
#     if parts[0] == "api":
#         parts = parts[1:]
#
#     system = parts[0] if len(parts) > 0 else None
#     action = parts[1] if len(parts) > 1 else None
#
#     print("DEBUG:", system, action, method)
#
#     if system == "reports":
#         return handle(system, action, body, method)
#
#     elif system == "interns":
#         return handle(system, action, body, method)
#
#     else:
#         return {"error": "Unknown system"}


# =========================
# ✅ NEW CLEAN ROUTER
# =========================

from connectors.ExpressConnect import forward_report_to_express   # ✅ FIXED import


def route_request(target, data, file=None):

    print("\n🧠 ROUTER TARGET:", target)
    print("🧠 ROUTER DATA:", data)

    if target == "express":
        return forward_report_to_express(data, file)

    print("❌ ROUTER: UNKNOWN TARGET")

    return {"error": f"Unknown target: {target}"}