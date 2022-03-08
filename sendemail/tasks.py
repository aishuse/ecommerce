from django.contrib.auth import get_user_model

from celery import shared_task
from django.core.mail import send_mail
from ecommerce import settings


@shared_task(bind=True)
def test_func(self):
    #operations
    for i in range(10):
        print(i)
    return "Done"


@shared_task(bind=True)
def send_emails_tasks(self,email, subject, message):
    # import pdb
    # pdb.set_trace()
    users = email.split(",")
    for user in users:
        mail_subject = subject
        message = message
        to_email = user
        send_mail(
            subject=mail_subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[to_email],
            fail_silently=True,
        )
    return "Done"



# def send_mail_func(self):
#     users = get_user_model().objects.all()
#     for user in users:
#         mail_subject = "Hi! Celery Testing"
#         message = "If you are liking my content, please hit the like button and do subscribe to my channel"
#         # to_email = user.email
#         send_mail(
#             subject = mail_subject,
#             message=message,
#             from_email=settings.EMAIL_HOST_USER,
#             # recipient_list=[to_email],
#
#             recipient_list=['babyaishuu@gmail.com', 'aiswarya180@gmail.com', 'booklandz911@gmail.com'],
#             fail_silently=True,
#         )
#     return "Done"
#

