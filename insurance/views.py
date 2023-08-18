from insurance.models import Client, Insurance
from insurance.serializers import ClientSerializer, InsuranceSerializer

from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions


class ClientViewSet(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [permissions.IsAuthenticated]


class InsuranceViewSet(ModelViewSet):
    queryset = Insurance.objects.all()
    serializer_class = InsuranceSerializer
    permission_classes = [permissions.IsAuthenticated]
