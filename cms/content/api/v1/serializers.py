from rest_framework import serializers
from cms.content.models import Media, MediaFile, CEOProfile, Contact, Testimonial, Service, TeamMember, Activity


class MediaFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaFile
        fields = ['id', 'file', 'media']
        read_only_fields = ['id']

    def validate_file(self, value):
        # Fetch the related `Media` instance
        media_id = self.initial_data.get('media')  # Get media ID from request data
        media = Media.objects.filter(id=media_id).first()

        if not media:
            raise serializers.ValidationError("Invalid media ID provided.")

        # Extract the file extension
        file_extension = value.name.split('.')[-1].lower() if '.' in value.name else ''
        allowed_extensions = MediaFile.ALLOWED_EXTENSIONS.get(media.media_type, [])

        # Check if the file extension is valid
        if f".{file_extension}" not in allowed_extensions:
            raise serializers.ValidationError(
                f"Invalid file type for {media.media_type}. "
                f"Allowed types: {', '.join(allowed_extensions)}"
            )

        return value



class MediaSerializer(serializers.ModelSerializer):
    files = MediaFileSerializer(many=True, read_only=True)

    class Meta:
        model = Media
        fields = ['id', 'title', 'media_type', 'slug', 'files']
        read_only_fields = ['id', 'slug']


class CEOProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CEOProfile
        fields = ['id', 'slug', 'name', 'photo', 'title', 'content', 'linkedin', 'twitter', 'facebook', 'instagram']

    def validate(self, attrs):
        if CEOProfile.objects.exists() and not self.instance:
            raise serializers.ValidationError("There can only be one CEOProfile in the system.")
        
        social_media_fields = ['linkedin', 'twitter', 'facebook', 'instagram']
        if not any(attrs.get(field) for field in social_media_fields):
            raise serializers.ValidationError("At least one social media link must be provided.")
        return attrs


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'name', 'slug', 'email', 'phone', 'subject', 'message'] 


class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = ['id', 'name', 'designation', 'company', 'message', 'image', 'rating', 'is_approved', 'created', 'updated']


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'title', 'description', 'icon', 'price', 'duration', 'is_active', 'created', 'updated']


class TeamMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMember
        fields = ['id', 'name', 'email', 'phone', 'role', 'profile_picture', 'bio', 'date_joined', 'is_active', 'created', 'updated']

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ['id', 'title', 'category', 'image', 'status', 'start_date', 'end_date', 'description', 'created', 'updated']       