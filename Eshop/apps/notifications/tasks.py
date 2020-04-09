from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_email_task():
    send_mail(
        'Celery Task Worked!',
        'This is proof the task worked.',
        'your gmail acc',
        ['receiver']
    )
    return None
