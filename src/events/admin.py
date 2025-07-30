from django.contrib import admin

from .models import Event, Place


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("title", "date", "status", "place")
    list_filter = ("status", "place")


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ("title",)
