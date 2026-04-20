import requests
def forward_report_to_express(data, file=None):

    print("\n🚀 CONNECTOR SENDING:", data)

    response = requests.post(
        "http://127.0.0.1:4000/api/reports",

        data=data,   # ✅ USE WHAT YOU RECEIVED DIRECTLY

        files={
            "pdf_file": file.file
        } if file else None
    )

    print("📡 RESPONSE:", response.text)

    return response.json()