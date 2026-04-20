from django.urls import path
from .views import  forward_report


urlpatterns = [

    # =========================
    # ✅ SPECIFIC ROUTES FIRST (VERY IMPORTANT)
    # =========================

    path('forward/', forward_report),   # ✅ FIXED SPELLING

    # =========================
    # ⚠️ CATCH-ALL ROUTE LAST
    # =========================

    #path('', api_gateway),
    #path('<path:path>/', api_gateway),
]