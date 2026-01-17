from django.contrib import admin
from .models import DeliveryOrder, DeliveryAgent

admin.site.register(DeliveryOrder)
admin.site.register(DeliveryAgent)