from rest_framework import serializers
from .models import Bank,SalaryRange

class SalaryRangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalaryRange
        fields = '__all__'

class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = ['id','name','fd_interest_rate','rd_interest_rate','savings_interest_rate']

'''class InvestmentRecommendationSerializer(serializers.ModelSerializer):
    salary_range = SalaryRangeSerializer()
    bank = BankSerializer()
    
    class Meta:
        model = InvestmentRecommendation
        fields = '__all__'''