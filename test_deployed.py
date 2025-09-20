import requests
import json

# Test the deployed Azure Function
# Replace with your actual function URL and key
url = "https://your-function-app.azurewebsites.net/api/send_email?code=YOUR_FUNCTION_KEY_HERE"
payload = {
    "to_email": "recipient@example.com",
    "subject": "Test Email from Deployed Azure Function", 
    "message": "Hello! This is a test email sent from your deployed Azure Function in the cloud!"
}

try:
    response = requests.post(url, json=payload)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text}")
except Exception as e:
    print(f"Error: {str(e)}")
