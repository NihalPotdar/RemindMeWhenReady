import credentials
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import json

def hello_world():
    return str(send_email(str(request.get_json())))

def send_email(body):
    # creating the send grid service
    sendGrid = SendGridAPIClient(credentials.sendGridKey)

    message = Mail(
        from_email='nihalpot2002@gmail.com',
        to_emails='nihalpot2002@gmail.com',
        subject='Twitter Updates',
        html_content='<strong>'+body+'<strong>')
    try:
        response = sendGrid.send(message)
        return str(response.status_code)
    except Exception as e:
        return str(e)