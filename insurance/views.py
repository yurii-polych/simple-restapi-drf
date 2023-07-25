from insurance.models import Client, Insurance
from insurance.serializers import ClientSerializer, InsuranceSerializer

from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet


class ClientViewSet(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class InsuranceViewSet(ModelViewSet):
    queryset = Insurance.objects.all()
    serializer_class = InsuranceSerializer
