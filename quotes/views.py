from django.shortcuts import render
from .services.api_clients.client import consult_marcas
# Create your views here.

def home(request):
    return render(request, 'home.html', {})