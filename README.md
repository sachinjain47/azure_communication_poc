# Azure Communication Services Email POC

A Proof of Concept (POC) project demonstrating how to send emails using Azure Communication Services with Azure Functions.

## 🚀 Features

- **Azure Functions HTTP Trigger**: REST API endpoint for sending emails
- **Azure Communication Services**: Email delivery service integration
- **Python Implementation**: Built with Python 3.10+
- **JSON API**: Simple JSON-based email sending interface
- **Error Handling**: Comprehensive error handling and validation
- **Cloud Deployment Ready**: Configured for Azure Function App deployment

## 📧 API Usage

### Endpoint
```
POST /api/send_email
```

### Request Body
```json
{
    "to_email": "recipient@example.com",
    "subject": "Your Email Subject",
    "message": "Your email message content"
}
```

### Response
**Success (200):**
```json
{
    "message": "Email sent successfully",
    "operation_id": "{'id': 'uuid-here', 'status': 'Succeeded', 'error': None}"
}
```

**Error (400/500):**
```json
{
    "error": "Error description"
}
```

## 🛠️ Project Structure

```
azure-communication-poc/
├── send_email/
│   ├── __init__.py          # Main Azure Function code
│   └── function.json        # Function binding configuration
├── requirements.txt         # Python dependencies
├── host.json               # Azure Functions host configuration
├── local.settings.json     # Local development settings (excluded from git)
├── test_email.py           # Local testing script
├── test_deployed.py        # Deployed function testing script
└── README.md               # This file
```

## 📦 Dependencies

- `azure-functions`: Azure Functions runtime support
- `azure-communication-email`: Azure Communication Services Email client

## 🔧 Local Development

### Prerequisites
- Python 3.10+
- Azure Functions Core Tools
- Azure CLI

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/sachinjain47/azure_communication_poc.git
   cd azure_communication_poc
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure local settings:
   - Copy `local.settings.json.template` to `local.settings.json`
   - Add your Azure Communication Services connection string and sender address

4. Run locally:
   ```bash
   func start
   ```

5. Test the function:
   ```bash
   python test_email.py
   ```

## ☁️ Azure Deployment

### Prerequisites
- Azure subscription
- Azure Communication Services resource
- Azure Function App (Linux, Python 3.11)

### Deploy
```bash
func azure functionapp publish <your-function-app-name>
```

### Configure App Settings
Set the following application settings in your Azure Function App:
- `COMMUNICATION_SERVICES_CONNECTION_STRING`: Your Azure Communication Services connection string
- `COMMUNICATION_SERVICES_SENDER_ADDRESS`: Your verified sender email address

## 🔐 Authentication

The deployed function uses Azure Functions key-based authentication. Include the function key in your requests:

```
POST https://your-function-app.azurewebsites.net/api/send_email?code=your-function-key
```

## 🧪 Testing

### Local Testing
```bash
python test_email.py
```

### Deployed Testing
```bash
python test_deployed.py
```

## 📝 Configuration

### Azure Communication Services Setup
1. Create an Azure Communication Services resource
2. Add an email domain (Azure-managed or custom domain)
3. For custom domains, verify DNS records (TXT, SPF, DKIM)
4. Get the connection string from the Communication Services resource

### Function App Configuration
- Runtime: Python 3.11
- OS: Linux
- Plan: Consumption (Y1) or Premium
- Authentication Level: Function (requires key)

## 🚨 Important Notes

- **Sender Verification**: Ensure your sender domain is verified in Azure Communication Services
- **Rate Limits**: Be aware of Azure Communication Services rate limits
- **Cost Management**: Monitor usage to avoid unexpected charges
- **Security**: Keep connection strings and function keys secure

## 📄 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📧 Support

For issues and questions, please open an issue in this repository.

---

**Built with ❤️ using Azure Communication Services and Azure Functions**