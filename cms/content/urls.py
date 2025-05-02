from django.urls import path
from cms.content.api.v1.views import (
    MediaListAPIView, MediaListCreateAPIView, MediaRetrieveUpdateDestroyAPIView,
    CEOProfileListAPIView, CEOProfileListCreateAPIView, CEOProfileRetrieveUpdateDestroyAPIView,  ContactListAPIView, ContactListCreateAPIView,
    ContactRetrieveUpdateDestroyAPIView, TestimonialListAPIView, TestimonialListCreateAPIView, TestimonialRetrieveUpdateDestroyAPIView, ServiceListAPIView,
    ServiceListCreateAPIView, ServiceRetrieveUpdateDestroyAPIView, TeamMemberListAPIView, TeamMemberListCreateAPIView, TeamMemberRetrieveUpdateDestroyAPIView,
    ActivityAPIView, LatestActivityAPIView
)
app_name = "content"
urlpatterns = [
    # Media URLs
    path('media/', MediaListAPIView.as_view(), name='media-list'),
    path('media/create/', MediaListCreateAPIView.as_view(), name='media-create'),
    path('media/<slug:slug>/', MediaRetrieveUpdateDestroyAPIView.as_view(), name='media-detail'),


    # CEO URLs
    path('CEOProfile/', CEOProfileListAPIView.as_view(), name='ceo-list'),
    path('CEOProfile/create/', CEOProfileListCreateAPIView.as_view(), name='ceo-create'),
    path('CEOProfile/<slug:slug>/', CEOProfileRetrieveUpdateDestroyAPIView.as_view(), name='ceo-detail'),

    # Contact URLs
    path('contact/', ContactListAPIView.as_view(), name='contact-list'),
    path('contact/create/', ContactListCreateAPIView.as_view(), name='contact-create'),
    path('contact/<slug:slug>/', ContactRetrieveUpdateDestroyAPIView.as_view(), name='contact-detail'),

    # Testimonial URLs
    path('testimonials/', TestimonialListAPIView.as_view(), name='testimonial-list'),
    path('testimonials/create/', TestimonialListCreateAPIView.as_view(), name='testimonial-create'),
    path('testimonials/<slug:slug>/', TestimonialRetrieveUpdateDestroyAPIView.as_view(), name='testimonial-detail'),

    # Service URLs
    path('services/', ServiceListAPIView.as_view(), name='service-list'),
    path('services/create/', ServiceListCreateAPIView.as_view(), name='service-create'),
    path('services/<slug:slug>/', ServiceRetrieveUpdateDestroyAPIView.as_view(), name='service-detail'),

    # TeamMember URLs
    path('team-members/', TeamMemberListAPIView.as_view(), name='team-member-list'),
    path('team-members/create/', TeamMemberListCreateAPIView.as_view(), name='team-member-create'),
    path('team-members/<slug:slug>/', TeamMemberRetrieveUpdateDestroyAPIView.as_view(), name='team-member-detail'),

    # Activity
    path('activities/', ActivityAPIView.as_view(), name='activities'),
    path('activities/latest/', LatestActivityAPIView.as_view(), name='latest-activities'),

]


