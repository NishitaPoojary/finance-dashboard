from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Salary Range Model
class SalaryRange(models.Model):
    label = models.CharField(max_length=50) # e.g., "Below 30,000", "30,000 - 70,000", etc.
    min_salary = models.IntegerField()
    max_salary = models.IntegerField()

    def __str__(self):
        return self.label

# Bank Model
class Bank(models.Model):
    name = models.CharField(max_length=100)
    fd_interest_rate = models.FloatField() # Fixed Deposit interest rate
    rd_interest_rate = models.FloatField() # Recurring Deposit interest rate
    savings_interest_rate = models.FloatField()

    def __str__(self):
        return self.name

# Investment Recommendation Model
class InvestmentRecommendation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    salary_range = models.ForeignKey(SalaryRange, on_delete=models.CASCADE)
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    recommendation_type = models.CharField(max_length=50) # FD, RD, or Savings
    projected_earning = models.FloatField()
    duration_months = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.recommendation_type}"


