from integration.router import route_request   # ✅ only import what we use
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from integration.services.campusroute import handle_campus_route


@csrf_exempt
def receive_student(request):
    if request.method != "POST":
        return JsonResponse({"error": "Only POST is allowed"}, status=405)

    try:
        payload = json.loads(request.body.decode("utf-8"))
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON"}, status=400)

    result = handle_campus_route(payload)

    if result.get("ok"):
        return JsonResponse(result, status=200)

    return JsonResponse(result, status=400)
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

        # GUARD (VERY IMPORTANT)
        if not data["title"]:
            print("INVALID DATA FROM DJANGO")
            return JsonResponse({"error": "Invalid data"}, status=400)

        result = route_request("express", data, file)

        print("📡 GATEWAY RESPONSE:", result)

        return JsonResponse(result)

    return JsonResponse({"error": "Only POST allowed"})