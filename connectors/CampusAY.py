import json
from urllib import request
from urllib.error import HTTPError, URLError


YAOUNDE_URL = "http://127.0.0.1:3001/api/students/receive"


def send_to_yaounde(payload):
    data = json.dumps(payload).encode("utf-8")

    req = request.Request(
        YAOUNDE_URL,
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


def delete_in_yaounde(student_id):
    req = request.Request(
        f"{YAOUNDE_URL.rsplit('/receive', 1)[0]}/receive/{student_id}",
        method="DELETE",
    )

    try:
        with request.urlopen(req, timeout=10) as response:
            raw = response.read().decode("utf-8")
            return {
                "ok": True,
                "status_code": response.status,
                "response": json.loads(raw),
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
