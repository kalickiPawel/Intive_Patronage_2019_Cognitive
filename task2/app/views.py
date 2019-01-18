from django.http import JsonResponse
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Earning
from .models import Estimate

# Create your views here.
def home(request):
    return render(request, 'app/base.html', {})

def charts(request):
    return render(request, 'app/charts.html', {})
    
def data_table(request):

    estimate = Estimate.objects.all()
    earnings = Earning.objects.all()

    return render(request, 'app/data_table.html', {'earnings': earnings, 'estimate': estimate})

class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        labels = ["Red", "Blue", "Yellow", "Green", "Purple", "Orange"]
        data = {
                "labels": labels,
                "earning": Earning.objects.all(),
                "estimate": Estimate.objects.all()
        }
        return Response(data)