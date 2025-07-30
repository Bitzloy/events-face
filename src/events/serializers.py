from rest_framework import serializers

from .models import Event, Place


class EventSerializer(serializers.ModelSerializer):
    place_title = serializers.CharField(source='Place.title', read_only=True)

    class Meta:
        model = Event
        fields = ["id", "title", "date", "status", "place", "place_title"]
