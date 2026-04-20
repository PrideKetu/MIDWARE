from integration.router import route_request   # ✅ only import what we use
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


# =========================
# ❌ OLD GENERIC API GATEWAY (DISABLED)
# =========================

# from integration.router import process_request, route_request
#
# @csrf_exempt
# def api_gateway(request, path=""):
#
#     body = {}
#
#     if request.method in ["POST", "PUT", "PATCH"]:
#         try:
#             body = json.loads(request.body)
#         except:
#             body = {}
#
#     response = process_request(path, body, request.method)
#
#     return JsonResponse(response, safe=False)


# =========================
# ✅ ACTIVE PIPELINE ENTRY POINT
# =========================

@csrf_exempt
def forward_report(request):

    if request.method == "POST":

        data = {
            "title": request.POST.get("title"),
            "intern_id": request.POST.get("intern_id")
        }

        file = request.FILES.get("pdf_file")

        print("\n🔥 GATEWAY RECEIVED:", data)

        # 🛑 GUARD (VERY IMPORTANT)
        if not data["title"]:
            print("❌ INVALID DATA FROM DJANGO")
            return JsonResponse({"error": "Invalid data"}, status=400)

        result = route_request("express", data, file)

        print("📡 GATEWAY RESPONSE:", result)

        return JsonResponse(result)

    return JsonResponse({"error": "Only POST allowed"})