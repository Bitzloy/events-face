import uuid

from django.db import models


class Place(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Event(models.Model):
    class Status(models.TextChoices):
        OPEN = "open", "Open"
        CLOSED = "closed", "Closed"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    date = models.DateTimeField()
    status = models.CharField(max_length=6, choices=Status.choices, default=Status.OPEN)
    place = models.ForeignKey(
        Place, null=True, blank=True, on_delete=models.SET_NULL, related_name="events"
    )

    def __str__(self):
        return self.title
