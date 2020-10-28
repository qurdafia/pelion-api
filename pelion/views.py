from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets
from . import serializers
from . import models


def index(request):
    return render(request, "pelion/index.html", {})


class EventViewSet(viewsets.ModelViewSet):
    """Handle creating and update profiles"""

    serializer_class = serializers.EventSerializer
    queryset = models.Event.objects.all()
    search_fields = ('deviceName', 'personName')
