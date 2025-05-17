from django.urls import path, include
from rest_framework import routers
from .views import BankViewSet, SalaryRangeViewSet, InvestmentRecommendationViewSet

router = routers.DefaultRouter()
router.register(r'banks', BankViewSet)
router.register(r'salary-ranges', SalaryRangeViewSet)
router.register(r'investments', InvestmentRecommendationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]