from django.shortcuts import render
from .models import EstimateEarning

# Create your views here.
def index(request):
    estimate_earnings = EstimateEarning.objects.all()
    return render(request, 'index.html', {'estimate': estimate_earnings})