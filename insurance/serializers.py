from rest_framework import serializers
from insurance.models import Client, Insurance


class ClientSerializer(serializers.Serializer):
    class Meta:
        model = Client
        fields = '__all__'


class InsuranceSerializer(serializers.Serializer):
    class Meta:
        model = Insurance
        fields = '__all__'
