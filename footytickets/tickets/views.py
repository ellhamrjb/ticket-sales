from django.shortcuts import render
from rest_framework import viewsets
from .models import Event,Tickets
from .serializers import EventSerializer,TickestSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset=Event.objects.all()
    serializer_class=EventSerializer
    
class TicketsViewSet(viewsets.ModelViewSet):
    queryset=Tickets.objects.all()
    serializer_class=TickestSerializer
    
    
