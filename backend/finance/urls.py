from django.urls import path
from .views import SalaryRangeList, BankList, InvestmentRecommendationView

urlpatterns = [
    path('salary-ranges/', SalaryRangeList.as_view(), name='salary-ranges'),
    path('banks/', BankList.as_view(), name='banks'),
    path('recommend/', InvestmentRecommendationView.as_view(), name='recommend'),
]