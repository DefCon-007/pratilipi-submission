from django.core.mail import send_mass_mail, send_mail
import sendgrid
from sendgrid.helpers.mail import *
from django.conf import settings
def sendMails(emailList, subject, body) :
    dataTuple = [(subject, body, "<admin> pvradmin@defcon007.com",e) for e in emailList ]
    send_mass_mail( dataTuple, fail_silently=True )


def sendSingleMail(email,subject,body) :
    sg = sendgrid.SendGridAPIClient(apikey=settings.SENDGRID_API_KEY)
    from_email = Email("pvradmin@defcon007.com")
    to_email = Email(email)
    subject = subject
    content = Content("text/plain", body)
    mail = Mail(from_email, subject, to_email, content)
    mail.reply_to = Email("ayushgoyal.iitkgp@gmail.com")
    response = sg.client.mail.send.post(request_body=mail.get())
