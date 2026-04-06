from rest_framework.views import APIView
from rest_framework.response import Response
from records.models import Record
from django.db.models import Sum

class DashboardSummary(APIView):
    def get(self, request):
        income = Record.objects.filter(type='income').aggregate(Sum('amount'))['amount__sum'] or 0
        expense = Record.objects.filter(type='expense').aggregate(Sum('amount'))['amount__sum'] or 0

        return Response({
            "total_income": income,
            "total_expense": expense,
            "net_balance": income - expense
        })