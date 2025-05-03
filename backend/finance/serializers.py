from rest_framework import serializers
from .models import SalaryRange, Bank, InvestmentRecommendation

class SalaryRangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalaryRange
        fields = '__all__'

class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = '__all__'

class InvestmentRecommendationSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvestmentRecommendation
        fields = '__all__'