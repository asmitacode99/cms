from rest_framework.generics import (RetrieveUpdateDestroyAPIView, ListAPIView, ListCreateAPIView)
from rest_framework.response import Response
from rest_framework import status
from cms.content.models import Media, MediaFile,  CEOProfile, Contact, Testimonial, Service, TeamMember, Activity
from cms.content.api.v1.serializers import MediaSerializer, CEOProfileSerializer, ContactSerializer, TestimonialSerializer, ServiceSerializer, TeamMemberSerializer, MediaFileSerializer, ActivitySerializer
from cms.content.api.v1.usecases import CEOProfileQuerysetUseCase
from rest_framework.permissions import IsAuthenticated


# Media Views
class MediaListAPIView(ListAPIView):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer

class MediaListCreateAPIView(ListCreateAPIView):
    queryset = MediaFile.objects.all()
    serializer_class = MediaFileSerializer


class MediaRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer
    lookup_field = 'slug'


#CEO Views
class CEOProfileListAPIView(ListAPIView):
    queryset = CEOProfile.objects.all()
    serializer_class = CEOProfileSerializer
  
class CEOProfileListCreateAPIView(ListCreateAPIView):
    queryset = CEOProfile.objects.all()
    serializer_class = CEOProfileSerializer

class CEOProfileRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = CEOProfile.objects.all()
    serializer_class = CEOProfileSerializer
    lookup_field = 'slug'


# Contact Views
class ContactListAPIView(ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    

class ContactListCreateAPIView(ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class ContactRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    lookup_field = 'slug'    


# Testimonial View
class TestimonialListAPIView(ListAPIView):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer

class TestimonialListCreateAPIView(ListCreateAPIView):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer

class TestimonialRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer
    lookup_field = 'slug'


# Service Views
class ServiceListAPIView(ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class ServiceListCreateAPIView(ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class ServiceRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    lookup_field = 'slug'


# TeamMember Views
class TeamMemberListAPIView(ListAPIView):
    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer

class TeamMemberListCreateAPIView(ListCreateAPIView):
    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer

class TeamMemberRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer
    lookup_field = 'slug'

class ActivityAPIView(ListAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class LatestActivityAPIView(ListAPIView):
    serializer_class = ActivitySerializer

    def get_queryset(self):
        return Activity.objects.all().order_by('-created')[:5]