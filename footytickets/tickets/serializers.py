from rest_framework import serializers
from .models import Event, Tickets

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields= '__all__'
        
class TickestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tickets
        fields= '__all__'