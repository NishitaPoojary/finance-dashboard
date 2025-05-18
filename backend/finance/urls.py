from django.urls import path
from . import views

urlpatterns = [
    path('banks/', views.BankListAPIView.as_view(), name='bank-list'),
    path('salary-ranges/', views.SalaryRangeListAPIView.as_view(), name='salary-range-list'),
]