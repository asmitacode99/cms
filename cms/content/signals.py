from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from cms.content.models import Contact
from cms.core.emails import send_notification_email, get_admin_emails


@receiver(post_save, sender=Contact)
def send_contact_notification(sender, instance, created, **kwargs):
    if created:  # Check if the contact was created
        subject = f"New Contact Submission: {instance.subject}"
        message = f"New contact submission received. Here are the details:\n"

        # Prepare contact data to include in the email
        contact_data = {
            'Name': instance.name,
            'Email': instance.email,
            'Phone': instance.phone or 'N/A',
            'Subject': instance.subject,
            'Message': instance.message,
        }

        recipient_list = get_admin_emails()  # Get the list of admin email addresses
        send_notification_email(subject, message, contact_data, recipient_list)


@receiver(post_delete, sender=Contact)
def send_contact_deleted_notification(sender, instance, **kwargs):
    subject = 'Contact Deleted'
    message = "A contact has been deleted. Here are the details:\n"

    # Prepare contact data to include in the email
    contact_data = {
        'Name': instance.name,
        'Email': instance.email,
        'Phone': instance.phone or 'N/A',
        'Subject': instance.subject,
        'Message': instance.message,
    }

    recipient_list = get_admin_emails()  # Get the list of admin email addresses
    send_notification_email(subject, message, contact_data, recipient_list)
