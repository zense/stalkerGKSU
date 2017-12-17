from flask_mail import Message
from main import mail
import config
from main import app

def send_email(organisation, recipients):
    sender = config.ADMINS[0]
    subject = 'Results have been generated for ' + organisation
    text_body = """ Greetings from Zense,

                    We have completed your task in regards to %s
                    Please visit us back

                    Regards,
                    Team Stalker, Zense """ % str(organisation)
    msg = Message(subject, sender = sender, recipients = recipients)
    msg.body = text_body
    with app.app_context():
        mail.send(msg)
