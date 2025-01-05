from django.shortcuts import render
from .services.api_clients.client import brand_consultation
# Create your views here.

def home(request):
    return render(request, "home.html")

def marcas(request):
    vehicle_type = request.POST.get('veiculo')
    response = brand_consultation(vehicle_type=vehicle_type)
    return render(request, "brand.html", {"vehicle_type": vehicle_type, "list_brand": response})