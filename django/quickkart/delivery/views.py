from rest_framework import viewsets
from .models import DeliveryOrder, DeliveryAgent
from .serializers import DeliveryOrderSerializer, DeliveryAgentSerializer

class DeliveryAgentViewSet(viewsets.ModelViewSet):
    queryset = DeliveryAgent.objects.all()
    serializer_class = DeliveryAgentSerializer


class DeliveryOrderViewSet(viewsets.ModelViewSet):
    queryset = DeliveryOrder.objects.all()
    serializer_class = DeliveryOrderSerializer
