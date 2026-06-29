from django.contrib import admin

from .models import Event, Registration


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'location',
        'date',
        'organizer',
    )

    search_fields = (
        'title',
        'location',
    )

    list_filter = (
        'date',
        'organizer',
    )


@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):

    list_display = (
        'user',
        'event',
        'created_at',
    )

    search_fields = (
        'user__username',
        'event__title',
    )

    list_filter = (
        'created_at',
    )