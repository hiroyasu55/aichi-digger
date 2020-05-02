from flask import current_app
from flask_mail import Mail, Message


def send(recipients=[], subject='', body=''):

    mail = Mail(current_app)
    msg = Message(recipients=recipients,
                  body=body,
                  subject=subject)
    mail.send(msg)
