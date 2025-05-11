from rest_framework.views import APIView
from rest_framework.response import Response
from .models import SalaryRange, Bank, InvestmentRecommendation
from .serializers import SalaryRangeSerializer, BankSerializer, InvestmentRecommendationSerializer

class SalaryRangeList(APIView):
    def get(self, request):
        ranges = SalaryRange.objects.all()
        serializer = SalaryRangeSerializer(ranges, many=True)
        return Response(serializer.data)

class BankList(APIView):
    def get(self, request):
        banks = Bank.objects.all()
        serializer = BankSerializer(banks, many=True)
        return Response(serializer.data)

class InvestmentRecommendationView(APIView):
    def post(self, request):
        salary = request.data.get('salary')
        bank_id = request.data.get('bank')

        try:
            bank = Bank.objects.get(id=bank_id)
        except Bank.DoesNotExist:
            return Response({'error': 'Bank not found'}, status=404)

        recommendations = []

        if int(salary) < 30000:
            type = 'RD'
            rate = bank.rd_interest_rate
        else:
            type = 'FD'
            rate = bank.fd_interest_rate

        projected_return = int(salary) * (rate / 100)

        rec = InvestmentRecommendation.objects.create(
            bank=bank,
            recommendation_type=type,
            projected_return=projected_return
        )

        serializer = InvestmentRecommendationSerializer(rec)
        return Response(serializer.data)

