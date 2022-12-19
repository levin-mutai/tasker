from rest_framework import serializers

from .models import Client_messages,subscribe

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client_messages
        fields = '__all__'

class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = subscribe
        fields = '__all__'
