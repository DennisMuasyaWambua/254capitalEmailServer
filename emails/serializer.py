from rest_framework import serializers
from .models import LoanApplicationModel,ContactUsModel

class LoanApplicationSerializer(serializers.ModelSerializer):
  class Meta:
    model = LoanApplicationModel
    fields = '__all__'

class ContactUsSerializer(serializers.ModelSerializer):
  class Meta:
    model = ContactUsModel
    fields = '__all__'