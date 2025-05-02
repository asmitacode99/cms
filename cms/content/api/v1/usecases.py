from django.core.exceptions import ValidationError
from cms.core.usecases import BaseUseCase  # Replace this with your actual base use case or remove if unnecessary
from cms.content.models import CEOProfile

class CEOProfileQuerysetUseCase:
    def __init__(self, request):
        self.request = request

    def execute(self):
        self.is_valid()
        return self._get_queryset()

    def is_valid(self):
        user = self.request.user
        if not user.is_authenticated:
            raise ValidationError("User must be authenticated to access CEO Profile.")

    def _get_queryset(self):
        return CEOProfile.objects.all()

    