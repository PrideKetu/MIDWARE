import requests

BASE_URL = "http://127.0.0.1:8001/interns/"

def handle_request(method, path="", body=None):
    url = BASE_URL + path

    if method == "GET":
        return requests.get(url).json()

    elif method == "POST":
        return requests.post(url, json=body).json()