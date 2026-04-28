import json
from urllib import request
from urllib.error import HTTPError, URLError


DOUALA_URL = "http://127.0.0.1:3002/api/students/receive"


def send_to_douala(payload):
    data = json.dumps(payload).encode("utf-8")

    req = request.Request(
        DOUALA_URL,
        data=data,
        headers={"Content-Type": "application/json"},
        method="POST",
    )

    try:
        with request.urlopen(req, timeout=10) as response:
            body = response.read().decode("utf-8")
            return {
                "ok": True,
                "status_code": response.status,
                "response": json.loads(body),
            }
    except HTTPError as error:
        return {
            "ok": False,
            "error": f"HTTP error: {error.code}",
        }
    except URLError as error:
        return {
            "ok": False,
            "error": f"Connection error: {error.reason}",
        }
