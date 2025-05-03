from django.shortcuts import render
from rest_framework import viewsets
from .models import SalaryRange, Bank, InvestmentRecommendation
from .serializers import SalaryRangeSerializer, BankSerializer, InvestmentRecommendationSerializer

# Create your views here.

class SalaryRangeViewSet(viewsets.ModelViewSet):
    queryset = SalaryRange.objects.all()
    serializer_class = SalaryRangeSerializer

class BankViewSet(viewsets.ModelViewSet):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer

class InvestmentRecommendationViewSet(viewsets.ModelViewSet):
    queryset = InvestmentRecommendation.objects.all()
    serializer_class = InvestmentRecommendationSerializer

