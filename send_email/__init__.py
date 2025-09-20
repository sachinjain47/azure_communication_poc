import logging
import json
import os
import azure.functions as func
from azure.communication.email import EmailClient

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    try:
        # Parse request body
        req_body = req.get_json()
        to_email = req_body.get('to_email')
        subject = req_body.get('subject')
        message = req_body.get('message')
        
        # Validate required fields
        if not all([to_email, subject, message]):
            return func.HttpResponse(
                json.dumps({
                    'error': 'Missing required fields. Please provide to_email, subject, and message.'
                }),
                status_code=400
            )

        # Get connection string from app settings
        connection_string = os.environ["COMMUNICATION_SERVICES_CONNECTION_STRING"]
        sender_address = os.environ["COMMUNICATION_SERVICES_SENDER_ADDRESS"]
        
        # Create the EmailClient
        email_client = EmailClient.from_connection_string(connection_string)

        # Prepare the email message
        message = {
            "senderAddress": sender_address,
            "recipients": {
                "to": [{"address": to_email}]
            },
            "content": {
                "subject": subject,
                "plainText": message
            }
        }

        # Send the email
        poller = email_client.begin_send(message)
        result = poller.result()

        return func.HttpResponse(
            json.dumps({
                'message': 'Email sent successfully',
                'operation_id': str(result)
            }),
            mimetype="application/json",
            status_code=200
        )

    except Exception as e:
        logging.error(f'Error sending email: {str(e)}')
        return func.HttpResponse(
            json.dumps({
                'error': f'Failed to send email: {str(e)}'
            }),
            status_code=500
        )