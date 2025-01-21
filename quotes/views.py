from django.shortcuts import render
from .services.api_clients.client import brand_consultation, models_consultation, years_models_constultation, model_year_model_consultation
# Create your views here.

def home(request):
    return render(request, "home.html")

def brand(request):
    vehicle_type = request.POST.get('veiculo')
    response = brand_consultation(vehicle_type=vehicle_type)

    return render(
        request, "brand.html", {"vehicle_type": vehicle_type, "list_brand": response}
        )

def models(request):
    vehicle_type = request.POST.get("vehicle_type")
    id_brand = request.POST.get("id_marca")
    name_brand = request.POST.get("nome_marca")

    response = models_consultation(
        vehicle_type=vehicle_type, id_brand=id_brand
        ).get('modelos')

    return render(
        request, "models.html", {"list_models": response, "vehicle_type": vehicle_type, "id_brand": id_brand, "name_brand": name_brand}
        )

def models_years(request):
    vehicle_type = request.POST.get("tipo_veiculo")
    id_brand = request.POST.get("id_marca")
    name_model = request.POST.get("nome_modelo")
    id_models = request.POST.get("id_modelo")

    response = years_models_constultation(
        vehicle_type=vehicle_type, id_brand=id_brand, id_models=id_models
        )

    return render(
        request, "years_model.html", {"vehicle_type": vehicle_type, "id_brand": id_brand, "name_model": name_model, "id_model": id_models, "list_years_model": response}
        )

def model_year_value(request):
    vehicle_type = request.POST.get("tipo_veiculo")
    id_brand = request.POST.get("id_marca")
    id_model = request.POST.get("id_modelo")
    id_year = request.POST.get("id_ano")

    response = model_year_model_consultation(
        vehicle_type=vehicle_type, id_brand=id_brand, id_model=id_model, id_year=id_year
        )

    return render(
        request, "model_year_value.html", response
    )