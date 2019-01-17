from django.shortcuts import render
from .models import Earning

# Create your views here.
def home(request):
    return render(request, 'app/base.html', {})
    
def data_table(request):
    estimate_earnings = Earning.objects.all()
    return render(request, 'app/data_table.html', {'estimate': estimate_earnings})

def histograms(request):
    temp = 0
    return render(request, 'app/histograms.html', {'variable': temp})