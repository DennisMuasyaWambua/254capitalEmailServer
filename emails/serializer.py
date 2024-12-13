from rest_framework import serializers
from .models import LoanApplicationModel

class LoanApplicationSerializer(serializers.ModelSerializer):
  class Meta:
    model = LoanApplicationModel
    fields = '__all__'