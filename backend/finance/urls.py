from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SalaryRangeViewSet, BankViewSet, InvestmentRecommendationViewSet

router = DefaultRouter()
router.register(r'salary', SalaryRangeViewSet)
router.register(r'banks', BankViewSet)
router.register(r'investments', InvestmentRecommendationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]