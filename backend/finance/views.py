from rest_framework import viewsets
from .models import SalaryRange, Bank, InvestmentRecommendation
from .serializers import SalaryRangeSerializer, BankSerializer, InvestmentRecommendationSerializer

class SalaryRangeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SalaryRange.objects.all()
    serializer_class = SalaryRangeSerializer

class BankViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer

class InvestmentRecommendationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = InvestmentRecommendation.objects.all()
    serializer_class = InvestmentRecommendationSerializer