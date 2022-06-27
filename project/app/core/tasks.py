from celery import shared_task

from . import mail

@shared_task
def send_email(email):
    print('dentro da funcao')
    return mail.core_notification(email)