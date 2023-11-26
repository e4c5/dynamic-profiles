from django.shortcuts import render

from rest_framework import viewsets
from .models import Contact, Person
from .serializers import PersonSerializer, ContactSerializer

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = PersonSerializer    