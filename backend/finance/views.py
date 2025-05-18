from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Bank, SalaryRange
from .serializers import BankSerializer, SalaryRangeSerializer

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