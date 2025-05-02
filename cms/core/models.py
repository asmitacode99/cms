from django.utils import timezone
from django.db import models
import uuid
from django.core.exceptions import ValidationError as DjangoValidationError
from django.utils.translation import gettext_lazy as _

# Create your models here.

class BaseModel(models.Model):
    """
    Base Model that will be used in this project
    """
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    is_archived = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, null= True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField( unique=True, null=True, blank=True,)
    class Meta:
        abstract=True

    def archive(self):
        if self.is_archived:
            raise DjangoValidationError({
                'non_field_errors': _('Failed - it is already archived.')
            })
        self.is_archived = True
        self.updated = timezone.now()
        self.save(update_fields=['is_archived', 'updated'])

    def restore(self):
        if not self.is_archived:    
            raise DjangoValidationError({
                'non_field_errors': _('Failed - it is already restored.')
            })
        self.is_archived = False
        self.updated = timezone.now()
        self.save(update_fields=['is_archived', 'updated'])

