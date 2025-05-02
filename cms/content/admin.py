from django.contrib import admin
from cms.content.models import Media, CEOProfile, MediaFile, Testimonial, Contact, Service, TeamMember, Location, Timeline, FAQ, Activity, BODMember, Appointment, TrustedParty, Subscription


class MediaFileInline(admin.TabularInline):
    model = MediaFile
    extra = 1

@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    inlines = [MediaFileInline]
    list_display = ('id', 'slug', 'title', 'media_type', 'created')
    search_fields = ('title', 'media_type')
    list_filter = ('media_type',)


@admin.register(CEOProfile)
class CEOProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'slug', 'name', 'title', 'created')  
    search_fields = ('name', 'title', 'content')  


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('id', 'slug', 'name', 'designation', 'company', 'rating', 'is_approved')
    list_filter = ('is_approved', 'rating')
    search_fields = ('name', 'designation', 'company', 'message')
    actions = ['approve_testimonials', 'unapprove_testimonials']


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'slug', 'name', 'email', 'subject')
    search_fields = ('name', 'email', 'subject', 'message') 


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'slug', 'title', 'price', 'duration', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('title', 'description')   


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('id', 'slug', 'name', 'role', 'email', 'is_active')
    search_fields = ('name', 'role', 'email')
    list_filter = ('is_active',)


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('id', 'slug', 'name', 'latitude', 'longitude') 
    search_fields = ('name',)  
    list_filter = ('name',) 


@admin.register(Timeline)
class TimelineAdmin(admin.ModelAdmin):
    list_display = ('id', 'slug', 'title', 'event_date', 'event_type', 'is_public')
    list_filter = ('event_type', 'is_public', 'event_date')
    search_fields = ('title', 'description')


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('id', 'slug', 'question', 'is_active', 'order')
    list_editable = ('is_active', 'order')
    search_fields = ('question', 'answer')
    ordering = ('order',)


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('id', 'slug', 'title', 'description')
    search_fields = ('title', 'description')

@admin.register(BODMember)
class BODMemberAdmin(admin.ModelAdmin):
    list_display = ('id', 'slug', 'name', 'position', 'email', 'phone', 'created')
    search_fields = ('name', 'position', 'email')


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'appointment_type', 'date', 'duration', 'is_confirmed', 'created',)
    search_fields = ('user__username', 'appointment_type', 'description')
    list_filter = ('appointment_type', 'is_confirmed', 'created')
    list_editable = ('is_confirmed',)


@admin.register(TrustedParty)
class TrustedPartyAdmin(admin.ModelAdmin):
    list_display = ('name', 'service_type', 'is_active')
    list_filter = ('service_type', 'is_active')
    search_fields = ('name', 'service_type')
    ordering = ('name',)
   
@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('subscriber', 'subscription_type', 'status', 'trusted_party', 'start_date', 'end_date', 'is_active')
    list_filter = ('status', 'is_active', 'trusted_party')
    search_fields = ('user__username', 'subscription_type', 'subscription_id')
    ordering = ('start_date',)
   