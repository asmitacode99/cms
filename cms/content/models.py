from django.db import models
from django_ckeditor_5.fields import CKEditor5Field  
from django.conf import settings
from django.core.exceptions import ValidationError
from cms.core.utils import generate_slug
from cms.core.models import BaseModel
from cms.blog.models import Category
from datetime import datetime


# Media model to represent images or files related to a page
class Media(BaseModel):
    MEDIA_CHOICES = [
        ('image', ('Image')),
        ('video', ('Video')),
        ('document', ('Document')),
    ]  
    title = models.CharField(max_length=255)
    media_type = models.CharField(max_length=10, choices=MEDIA_CHOICES)

    def __str__(self): 
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug: 
            self.slug = generate_slug(self.title)
        super().save(*args, **kwargs)  


class MediaFile(models.Model):
    ALLOWED_EXTENSIONS = {
        'image': ['.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff', '.webp'],
        'document': ['.pdf', '.docx', '.doc', '.xlsx', '.pptx', '.txt', '.rtf', '.odt'],
        'video': ['.mp4', '.mov', '.avi', '.mkv', '.flv', '.wmv', '.webm', '.mpeg', '.3gp'],
    }
    media = models.ForeignKey(Media, on_delete=models.CASCADE, related_name='files')
    file = models.FileField(upload_to='media_files/')

    def __str__(self):   
        return f"{self.media.title} - {self.file.name}"
    
    def clean(self):
        # Extract the file extension using string methods
        file_extension = self.file.name.split('.')[-1].lower() if '.' in self.file.name else ''
        allowed_extensions = self.ALLOWED_EXTENSIONS.get(self.media.media_type, [])
        
        # Check if the file extension is in the allowed list
        if f".{file_extension}" not in allowed_extensions:
            raise ValidationError(f"Invalid file type for {self.media.media_type}. Allowed types: {', '.join(allowed_extensions)}")

        super().clean()



class CEOProfile(BaseModel):
    name = models.CharField(max_length=255)   
    photo = models.ImageField(upload_to='ceo_images/') 
    title = models.CharField(max_length=255)  
    content = models.TextField(blank=True, null=True)  
    linkedin = models.URLField(blank=True, null=True) 
    twitter = models.URLField(blank=True, null=True)  
    facebook = models.URLField(blank=True, null=True)  
    instagram = models.URLField(blank=True, null=True)  

    def __str__(self):
        return self.name
     
    def clean(self):
        if CEOProfile.objects.exclude(pk=self.pk).exists():
            raise ValidationError("There can only be one CEOProfile in the system.")

        # Validate at least one contact or social media field is filled
        if not any([self.linkedin, self.twitter, self.facebook, self.instagram]):
            raise ValidationError("At least one social media link must be provided.")

        super().clean()

    def save(self, *args, **kwargs):
        if not self.slug: 
            self.slug = generate_slug(self.title) 

        self.clean() 
        super().save(*args, **kwargs)


class Testimonial(BaseModel):
    name = models.CharField(max_length=100, help_text="Name of the person giving the testimonial")
    designation = models.CharField(max_length=100, blank=True, null=True, help_text="Job title or role of the person")
    company = models.CharField(max_length=100, blank=True, null=True, help_text="Company or organization, if applicable")
    message = models.TextField(help_text="Testimonial content")
    image = models.ImageField(upload_to='testimonials/', blank=True, null=True, help_text="Photo of the person")
    rating = models.PositiveSmallIntegerField(default=5, help_text="Rating out of 5 (optional)")
    is_approved = models.BooleanField(default=False, help_text="Indicates if the testimonial is approved for display")

    def __str__(self):
        return f"{self.name} - {self.message[:50]}"   

    def save(self, *args, **kwargs):
        if not self.slug: 
            self.slug = generate_slug(self.name)
        super().save(*args, **kwargs)  


class Contact(BaseModel):
    name = models.CharField(max_length=255, help_text="Full name of the person contacting.")
    email = models.EmailField(help_text="Email address of the person.")
    phone = models.CharField(max_length= 15, blank=True, null=True, help_text="Optional phone number.")
    subject = models.CharField(max_length=255, help_text="Subject of the message.")
    message = models.TextField(help_text="Detailed message from the contact.")
   
    def __str__(self):
        return f"Message from {self.name} - {self.subject}"

    def save(self, *args, **kwargs):
        if not self.slug: 
            self.slug = generate_slug(self.name)
        super().save(*args, **kwargs)      


class Service(BaseModel):
    title = models.CharField(max_length=255, help_text="Title of the service.")
    description = models.TextField(help_text="Detailed description of the service.")
    icon = models.ImageField(upload_to="services/icons/", blank=True, null=True, help_text="Icon representing the service.")
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, help_text="Price of the service (if applicable).")
    duration = models.CharField(max_length=50, blank=True, null=True, help_text="Estimated duration of the service, e.g., '1 hour'.")
    is_active = models.BooleanField(default=True, help_text="Is the service currently active?")

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug: 
            self.slug = generate_slug(self.title)
        super().save(*args, **kwargs)  

 
class TeamMember(BaseModel):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    role = models.CharField(max_length=100)  
    profile_picture = models.ImageField(upload_to='team_members/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    date_joined = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} - {self.role}" 
    
    def save(self, *args, **kwargs):
        if not self.slug: 
            self.slug = generate_slug(self.name)
        super().save(*args, **kwargs)  


class Location(BaseModel):
    name = models.CharField(max_length=255)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return self.name or f"Lat: {self.latitude}, Lon: {self.longitude}"
    
    def save(self, *args, **kwargs):
        if not self.slug: 
            self.slug = generate_slug(self.name)
        super().save(*args, **kwargs)  


class Timeline(BaseModel):
    EVENT_TYPES = [
        ('milestone', 'Milestone'),
        ('achievement', 'Achievement'),
        ('update', 'Update'),
        ('general', 'General'),
    ]

    event_type = models.CharField(max_length=20, choices=EVENT_TYPES, default='general', help_text="Type of the event")
    title = models.CharField(max_length=255, help_text="Title of the timeline event")
    description = models.TextField(help_text="Detailed description of the event")
    event_date = models.DateField(help_text="Date of the event")
    related_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='timeline_events',
        help_text="Optional user related to this event"
    )
    image = models.ImageField(upload_to='timeline_images/', null=True, blank=True, help_text="Optional image for the event")
    is_public = models.BooleanField(default=True, help_text="Should this event be visible to everyone?")
    
    def __str__(self):
        return f"{self.title} ({self.event_date})"
    
    def save(self, *args, **kwargs):
        if not self.slug: 
            self.slug = generate_slug(self.title)
        super().save(*args, **kwargs)  


class FAQ(BaseModel):
    title = models.CharField(max_length=255, help_text="The title of the FAQ.")  # Added title field
    question = models.CharField(max_length=255, help_text="The FAQ question.")
    answer = models.TextField(help_text="The answer to the question.")
    is_active = models.BooleanField(default=True, help_text="Show this FAQ on the website.")
    order = models.PositiveIntegerField(default=0, help_text="Order of the FAQ in the list.")

    class Meta:
        ordering = ['order']  # Display FAQs in the specified order
        verbose_name = "FAQ"

    def __str__(self):
        return self.question       

    def save(self, *args, **kwargs):
        if not self.slug: 
            self.slug = generate_slug(self.order)
        super().save(*args, **kwargs)  


class Activity(BaseModel):
    title = models.CharField(max_length=255, help_text="Title of the activity (e.g., Health Camp, Tutoring).")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='activities', null=True, blank=True, help_text="Category of the activity.")
    image = models.ImageField(upload_to='activity_images/', null=True, blank=True, help_text="Optional image for the activity.")
    status = models.CharField(max_length=50, choices=[
        ('draft', 'Draft'),
        ('scheduled', 'Scheduled'),
        ('running', 'Running'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
        ('postponed', 'Postponed'),
    ], default='draft', help_text="Current status of the program.")

    start_date = models.DateField(null=True, blank=True, help_text="Start date of the activity.")
    end_date = models.DateField(null=True, blank=True, help_text="End date of the activity.")
    description = CKEditor5Field('description', config_name='extends')

    class Meta:
        ordering = ['title']  

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug: 
            self.slug = generate_slug(self.title)
        super().save(*args, **kwargs)  


class BODMember(BaseModel):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    photo = models.ImageField(upload_to='bod_photos/', blank=True, null=True)
    position = models.CharField(max_length=100, help_text="e.g., Chairman, Member, Treasurer")
    bio = models.TextField(blank=True, help_text="A short biography or description of the member")
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    order = models.PositiveIntegerField(default=0, help_text="Order of the member in the list.")

    class Meta:
        ordering = ['order']  
        verbose_name = "BODMember"

    def __str__(self):
        return f"{self.name} - {self.position}"
    
    def save(self, *args, **kwargs):
        if not self.slug: 
            self.slug = generate_slug(self.position)
        super().save(*args, **kwargs)  


class Appointment(BaseModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='appointments')
    appointment_type = models.CharField(max_length=100, choices=[
        ('video_call', 'Video Call'),
        ('in_person', 'In-person'),
        ('phone_call', 'Phone Call'),
        ('other', 'Other')
    ], default='video_call')

    zoom_url = models.URLField(blank=True, null=True, help_text="Zoom meeting URL")
    google_meet_url = models.URLField(blank=True, null=True, help_text="Google Meet URL")
    skype_url = models.URLField(blank=True, null=True, help_text="Skype meeting URL")
    in_person_location = models.CharField(max_length=255, blank=True, null=True, help_text="In-person meeting location")
    other_url = models.URLField(blank=True, null=True, help_text="URL for another platform or service")

    date = models.DateTimeField(help_text="Scheduled date and time for the appointment")
    duration = models.IntegerField(help_text="Duration of the appointment in minutes", default=30)  # Default 30 minutes
    description = models.TextField(blank=True, null=True, help_text="Optional description for the appointment")
    is_confirmed = models.BooleanField(default=False, help_text="Whether the appointment is confirmed")

    def __str__(self):
        return f"Appointment for {self.user.username} on {self.date}"

    def is_past(self):
        return self.date < datetime.now()

    def get_platform_url(self):
        if self.appointment_type == 'video_call':
            if self.zoom_url:
                return self.zoom_url
            elif self.google_meet_url:
                return self.google_meet_url
            elif self.skype_url:
                return self.skype_url
            return self.other_url
        elif self.appointment_type == 'in_person':
            return self.in_person_location
        return self.other_url

    def clean(self):
        url_fields = [
            self.zoom_url,
            self.google_meet_url,
            self.skype_url,
            self.in_person_location,
            self.other_url
        ]
        
        filled_fields = sum([1 for field in url_fields if field])

        if filled_fields > 1:
            raise ValidationError("Only one of the platform URLs or the in-person location can be filled.")


class TrustedParty(BaseModel):
    SERVICE_CHOICES = (
        ('payment', 'Payment Gateway'),
        ('authentication', 'Authentication Provider'),
        ('other', 'Other'),
    )
    
    name = models.CharField(max_length=255, help_text="Name of the trusted party (e.g., Stripe, PayPal, Google).")
    service_type = models.CharField(max_length=50, choices=SERVICE_CHOICES, help_text="The type of service provided by the trusted party.")
    api_key = models.CharField(max_length=255, null=True, blank=True, help_text="API key used to integrate with the third-party service.")
    is_active = models.BooleanField(default=True, help_text="Whether the trusted party is active.")

    def __str__(self):
        return f"{self.name} ({self.get_service_type_display()})"
    

class Subscription(BaseModel):
    SUBSCRIPTION_STATUS_CHOICES = (
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('cancelled', 'Cancelled'),
        ('pending', 'Pending'),
    )

    subscriber = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='subscriptions')
    subscription_type = models.CharField(max_length=100, help_text="The type of subscription (e.g., Basic, Premium).")
    start_date = models.DateField(help_text="The start date of the subscription.")
    end_date = models.DateField(help_text="The end date of the subscription.")
    status = models.CharField(max_length=50, choices=SUBSCRIPTION_STATUS_CHOICES, default='active', help_text="The current status of the subscription.")  
    trusted_party = models.ForeignKey(TrustedParty, on_delete=models.SET_NULL, null=True, blank=True, related_name='subscriptions', help_text="The trusted party used for this subscription (e.g., payment gateway).")   
    subscription_id = models.CharField(max_length=255, unique=True, help_text="The unique subscription ID from the trusted party service.")
    is_active = models.BooleanField(default=True, help_text="Whether the subscription is currently active.")

    def __str__(self):
        return f"{self.user.username} - {self.subscription_type} ({self.status})"
    
    def cancel_subscription(self):
        if self.trusted_party:
            pass
        self.status = 'cancelled'
        self.save()