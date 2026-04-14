import requests
import logging

# Express base URL (you can later move this to config/)
EXPRESS_BASE_URL = "http://localhost:3001"

logger = logging.getLogger(__name__)


def send_to_express(endpoint, data, method="POST"):
    """
    Generic connector to Express system
    """

    url = f"{EXPRESS_BASE_URL}{endpoint}"

    try:
        if method == "POST":
            response = requests.post(url, json=data, timeout=10)

        elif method == "GET":
            response = requests.get(url, params=data, timeout=10)

        else:
            return {
                "status": "error",
                "message": f"Unsupported method: {method}"
            }

        # Try to return JSON response from Express
        try:
            result = response.json()
        except Exception:
            result = {
                "raw_response": response.text
            }

        return {
            "status": "success",
            "express_status_code": response.status_code,
            "data": result
        }

    except requests.exceptions.ConnectionError:
        logger.error("Express system is down or unreachable")
        return {
            "status": "error",
            "message": "Express system not reachable"
        }

    except requests.exceptions.Timeout:
        return {
            "status": "error",
            "message": "Express request timed out"
        }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }


# -------------------------------
# SPECIFIC FUNCTION (your use case)
# -------------------------------

def forward_report_to_express(report_data):
    """
    This is your business-specific function
    """

    payload = {
        "title": report_data.get("title"),
        "intern_id": report_data.get("intern_id"),
        "description": report_data.get("description")
    }

    return send_to_express("/api/reports", payload, method="POST")