
from rest_framework import filters, viewsets
from rest_framework.pagination import PageNumberPagination

from .models import Event
from .serializers import EventSerializer


class EventPagination(PageNumberPagination):
    page_size = 10


class EventViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = EventSerializer
    pagination_class = EventPagination

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["title"]
    ordering_fields = ["date"]

    def get_queryset(self):
        return Event.objects.filter(status="open").select_related("place")
