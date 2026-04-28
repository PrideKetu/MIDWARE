from connectors.CampusAY  import send_to_yaounde
from connectors.CampusBD import send_to_douala


def handle_campus_route(payload):
    required_fields = [
        "student_id",
        "full_name",
        "campus",
        "program",
        "level",
        "registered_at",
    ]

    # Validate required fields
    missing = [field for field in required_fields if field not in payload]
    if missing:
        return {
            "ok": False,
            "error": "Missing required fields",
            "missing": missing,
        }

    source_campus = payload["campus"]

    # Determine target and route
    if source_campus == "Yaounde":
        target_campus = "Douala"
        connector_result = send_to_douala(payload)

    elif source_campus == "Douala":
        target_campus = "Yaounde"
        connector_result = send_to_yaounde(payload)

    else:
        return {
            "ok": False,
            "error": f"Unknown campus '{source_campus}'",
        }

    # Handle connector failure
    if not connector_result.get("ok"):
        return {
            "ok": False,
            "source_campus": source_campus,
            "target_campus": target_campus,
            "forward_result": connector_result,
        }

    return {
        "ok": True,
        "source_campus": source_campus,
        "target_campus": target_campus,
        "forward_result": connector_result,
    }