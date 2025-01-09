from django.shortcuts import render
from .services.api_clients.client import brand_consultation, models_consultation, years_models_constultation
# Create your views here.

def home(request):
    return render(request, "home.html")

def brand(request):
    vehicle_type = request.POST.get('veiculo')
    response = brand_consultation(vehicle_type=vehicle_type)
    return render(request, "brand.html", {"vehicle_type": vehicle_type, "list_brand": response})

def models(request):
    vehicle_type = request.POST.get("vehicle_type")
    id_brand = request.POST.get("id_brand")
    name_brand = request.POST.get("name_brand")

    response = models_consultation(vehicle_type=vehicle_type, id_brand=id_brand)["modelos"]

    return render(request, "models.html", {"list_models": response, "vehicle_type": vehicle_type, "id_brand": id_brand, "name_brand": name_brand})

def models_years(request):
    vehicle_type = request.POST.get("vehicle_type")
    id_brand = request.POST.get("id_brand")
    name_model = request.POST.get("name_model")
    id_model = request.POST.get("id_model")
    response = years_models_constultation(vehicle_type=vehicle_type, id_brand=id_brand, name_model=name_model, id_models=id_model)
    return render(request, "years_model.html", {"vehicle_type": vehicle_type, "id_brand": id_brand, "name_model": name_model, "id_model": id_model, "list_years_model": response})
