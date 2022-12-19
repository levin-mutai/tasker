from django.shortcuts import render
from rest_framework import generics

from .models import Client_messages,subscribe
from .serializers import MessageSerializer,SubscriptionSerializer
# Create your views here.

class MessageCreateViewset(generics.CreateAPIView):
    '''
    This allows the users to send messages to the company.
    '''
    queryset = Client_messages.objects.all()
    serializer_class = MessageSerializer
    http_method_names = ['post', 'options','head']

class SubscribeCreateViewset(generics.CreateAPIView):
    '''
    This allows the users to send messages to the company.
    '''
    queryset = subscribe.objects.all()
    serializer_class = SubscriptionSerializer
    http_method_names = ['post', 'options','head']