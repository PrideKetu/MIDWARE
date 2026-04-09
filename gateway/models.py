"""
from django.db import models

# Create your models here.
from .models import HR, School, Finance

def route_request(path, body):
    parts = path.split("/")
    if len(parts) < 2:
        return {"error": "Invalid route format"}
    
    system, action = parts[0], parts[1]

    # -------- HR --------
    if system == "hr":
        if action == "create":
            obj = HR.objects.create(name=body['name'], position=body['position'])
            return {"system": system, "action": action, "data": {"id": obj.id, "name": obj.name, "position": obj.position}}
        elif action == "fetch":
            records = HR.objects.all().values()
            return {"system": system, "action": action, "data": list(records)}

    # -------- School --------
    if system == "school":
        if action == "create":
            obj = School.objects.create(name=body['name'], students_count=body['students_count'])
            return {"system": system, "action": action, "data": {"id": obj.id, "name": obj.name, "students_count": obj.students_count}}
        elif action == "fetch":
            records = School.objects.all().values()
            return {"system": system, "action": action, "data": list(records)}

    # -------- Finance --------
    if system == "finance":
        if action == "create":
            obj = Finance.objects.create(transaction_id=body['transaction_id'], amount=body['amount'])
            return {"system": system, "action": action, "data": {"id": obj.id, "transaction_id": obj.transaction_id, "amount": obj.amount}}
        elif action == "fetch":
            records = Finance.objects.all().values()
            return {"system": system, "action": action, "data": list(records)}

    return {"error": "Unknown route"}"""