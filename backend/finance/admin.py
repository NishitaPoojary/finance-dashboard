from django.contrib import admin
from .models import SalaryRange, Bank, InvestmentRecommendation

# Register your models here.

admin.site.register(SalaryRange)
admin.site.register(Bank)
admin.site.register(InvestmentRecommendation)


