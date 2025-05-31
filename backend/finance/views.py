from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status 
from .models import Bank, SalaryRange
from .serializers import BankSerializer, SalaryRangeSerializer
import math 

class BankListAPIView(APIView):
    def get(self, request):
        banks = Bank.objects.all()
        serializer = BankSerializer(banks, many=True)
        return Response(serializer.data)

class SalaryRangeListAPIView(APIView):
    def get(self, request):
        ranges = SalaryRange.objects.all()
        serializer = SalaryRangeSerializer(ranges, many=True)
        return Response(serializer.data)

class InvestmentSuggestionsAPIView(APIView):
    def get(self, request):
        bank_id = request.query_params.get('bank_id')
        investment_amount_str = request.query_params.get('investment_amount')
        duration_months_str = request.query_params.get('duration_months', '12') # Default to 12 months for projection

        if not bank_id:
            return Response({"error": "bank_id is required."}, status=status.HTTP_400_BAD_REQUEST)
        if not investment_amount_str:
            return Response({"error": "investment_amount is required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            bank = Bank.objects.get(id=bank_id)
            investment_amount = float(investment_amount_str)
            duration_months = int(duration_months_str)
        except Bank.DoesNotExist:
            return Response({"error": "Bank not found."}, status=status.HTTP_404_NOT_FOUND)
        except ValueError:
            return Response({"error": "Invalid investment_amount or duration_months."}, status=status.HTTP_400_BAD_REQUEST)

        suggestions = []

        def calculate_projected_return(rate, amount, months):
            total_invested_principal = amount * months
            projected_gain = total_invested_principal * (rate / 100) * (duration_months / 12) 
            return total_invested_principal + projected_gain


        # FD Suggestion
        fd_projected_earning = calculate_projected_return(
            bank.fd_interest_rate, investment_amount, duration_months
        )
        suggestions.append({
            "bank_name": bank.name,
            "investment_type": "FDs",
            "interest_rate": bank.fd_interest_rate,
            "tenure_info": f"{duration_months} months", # Or more dynamic like "1-5 years"
            "expected_return_amount": round(fd_projected_earning, 2),
        })

        # RD Suggestion
        rd_projected_earning = calculate_projected_return(
            bank.rd_interest_rate, investment_amount, duration_months
        )
        suggestions.append({
            "bank_name": bank.name,
            "investment_type": "RDs",
            "interest_rate": bank.rd_interest_rate,
            "tenure_info": f"{duration_months} months",
            "expected_return_amount": round(rd_projected_earning, 2),
        })
        savings_projected_earning = calculate_projected_return(
            bank.savings_interest_rate, investment_amount, duration_months
        )
        suggestions.append({
            "bank_name": bank.name,
            "investment_type": "Savings",
            "interest_rate": bank.savings_interest_rate,
            "tenure_info": "Annualized", # Or "Average Daily Balance"
            "expected_return_amount": round(savings_projected_earning, 2),
        })

        return Response(suggestions, status=status.HTTP_200_OK)