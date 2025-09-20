import requests
import json

# Test the Azure Function locally
url = "http://localhost:7071/api/send_email"
payload = {
    "to_email": "test@example.com",
    "subject": "Test Email from Local Azure Function",
    "message": "Hello! This is a test email sent from your local Azure Function."
}

try:
    response = requests.post(url, json=payload)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text}")
except Exception as e:
    print(f"Error: {str(e)}")
