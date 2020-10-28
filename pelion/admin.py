from django.contrib import admin
from .models import Event, Attribute

# Register your models here.
admin.site.register(Attribute)
admin.site.register(Event)
