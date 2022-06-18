from core.celery import app
from django.core.mail import send_mail
from django.conf import settings

@app.task(bind=True)
def send_notification_about_task_to_email(*args,**kwargs):
        is_done = "Done" if kwargs.get("is_done") else "Not Done"
        id = kwargs.get('id')
        title = kwargs.get('title')
        email_to = kwargs.get('created_by_email')
        message = f"Task #{id} {title} is set as {is_done}"
        res = send_mail(f"Notification about task {id} {title}",from_email=settings.DEFAULT_FROM_EMAIL,message=message,recipient_list=[email_to])
        print(res)