from django.apps import apps
from django.conf import settings
from django.core.mail import send_mail


def get_admin_emails():
    User = apps.get_model(settings.AUTH_USER_MODEL)
    return User.objects.filter(is_superuser=True).values_list('email', flat=True)

def send_notification_email(subject, message, contact_data, recipient_list):
    message += "\n\nContact Details:\n"
    for key, value in contact_data.items():
        message += f"{key}: {value}\n"
    
    send_mail(
       subject,
       message,
       settings.EMAIL_HOST_USER,
       recipient_list,
       fail_silently=False, 
    )