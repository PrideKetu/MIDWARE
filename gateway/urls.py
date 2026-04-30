from django.urls import path
from .views import  forward_report

from gateway.views import receive_student, delete_student
urlpatterns = [

    # =========================
    # ✅ SPECIFIC ROUTES FIRST (VERY IMPORTANT)
    # =========================

    path('forward/', forward_report),   # ✅ FIXED SPELLING
    path("incoming/students/", receive_student, name="receive-student"),
    path("incoming/students/delete/", delete_student, name="delete-student"),

    # =========================
    #  CATCH-ALL ROUTE LAST
    # =========================

    #path('', api_gateway),
    #path('<path:path>/', api_gateway),
]