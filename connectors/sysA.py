import requests

BASE_URL = "http://127.0.0.1:8001"


# -----------------------------
# NORMAL JSON CRUD (interns, etc)
# -----------------------------
def handle(system, action, body, method):

    if action:
        url = f"{BASE_URL}/{system}/{action}/"
    else:
        url = f"{BASE_URL}/{system}/"

    try:

        if method == "GET":
            response = requests.get(url)

        elif method == "POST":
            response = requests.post(url, json=body)

        elif method == "PUT":
            response = requests.put(url, json=body)

        elif method == "DELETE":
            response = requests.delete(url)

        else:
            return {"error": "Unsupported method"}

        try:
            return response.json()
        except:
            return {
                "status_code": response.status_code,
                "text": response.text
            }

    except Exception as e:
        return {"error": str(e)}


# -----------------------------
# REPORT UPLOAD (PDF / FILES)
# -----------------------------
def forward_report_to_system(data):

    url = f"{BASE_URL}/upload/"

    files = {}
    if data.get("pdf_file"):
        files["pdf_file"] = data["pdf_file"]

    payload = {
        "title": data.get("title"),
        "intern": data.get("intern")
    }

    try:
        response = requests.post(url, data=payload, files=files)

        try:
            return response.json()
        except:
            return {
                "status_code": response.status_code,
                "text": response.text
            }

    except Exception as e:
        return {"error": str(e)}