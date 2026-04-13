import requests

BASE_URL = "http://127.0.0.1:8001"

def handle(system, action, body, method):
    
    if action:
        url = f"{BASE_URL}/{system}/{action}"
    else:
        url = f"{BASE_URL}/{system}/"    

    try:
        # Make the HTTP request
        if method == "GET":
            response = requests.get(url)
        elif method == "POST":
            response = requests.post(url, json=body)
        else:
            return {"error": "Unsupported HTTP method"}

        # Try parsing JSON
        try:
            return response.json()
        except ValueError:
            return {
                "error": "Reporting system returned invalid JSON",
                "status_code": response.status_code,
                "text": response.text
            }

    except requests.exceptions.RequestException as e:
        # Catch network errors
        return {"error": str(e)}
    except Exception as e:
        # Catch any other errors
        return {"error": str(e)}