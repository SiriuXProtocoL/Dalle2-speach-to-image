import requests
import json

# Define email parameters
to_address = "mdinzamamul.haque@etgworld.com"
subject = "Automatic email using Python"
message = "Hello, this is an automatic email sent using Python!"

# Define API endpoint and access token
api_endpoint = "https://graph.microsoft.com/v1.0/me/sendMail"
access_token = "<your_access_token_here>"

# Create email message in Microsoft Graph format
email = {
    "message": {
        "subject": subject,
        "body": {
            "contentType": "Text",
            "content": message
        },
        "toRecipients": [
            {
                "emailAddress": {
                    "address": to_address
                }
            }
        ]
    },
    "saveToSentItems": "true"
}

# Send email via Microsoft Graph API
headers = {
    "Authorization": "Bearer " + access_token,
    "Content-Type": "application/json"
}

response = requests.post(api_endpoint, headers=headers, data=json.dumps(email))

if response.status_code == 202:
    print("Email sent successfully!")
else:
    print("Error sending email: " + response.text)














#import smtplib
#from email.mime.text import MIMEText
#from email.mime.multipart import MIMEMultipart
#
## Define email parameters
#sender_email = "bebin.raju@etgworld.com"
#receiver_email = "mdinzamamul.haque@etgworld.com"
#subject = "Automatic email using Python"
#message = "Hello, this is an automatic email sent using Python!"
#
## Create a MIME message object
#msg = MIMEMultipart()
#msg['From'] = sender_email
#msg['To'] = receiver_email
#msg['Subject'] = subject
#
## Attach message to the MIME object
#msg.attach(MIMEText(message, 'plain'))
#
## Authenticate with Office 365 SMTP server
#username = "bebin.raju@etgworld.com"
#password = "Xtream$1234"
#smtp_server = "smtp.office365.com"
#smtp_port = 587
#
#with smtplib.SMTP(smtp_server, smtp_port) as server:
#    server.starttls()
#    server.login(username, password)
#    server.sendmail(sender_email, receiver_email, msg.as_string())
#
#print("Email sent successfully!")