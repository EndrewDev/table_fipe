import requests

BASE_URL = "https://parallelum.com.br/fipe/api/v1"

def brand_consultation(vehicle_type:str):
    formatted_address = f'{BASE_URL}/{vehicle_type}/marcas'
    response = requests.get(formatted_address)
    return response.json()

def models_consultation(vehicle_type:str, id_brand:str):
    formatted_address = f"{BASE_URL}/{vehicle_type}/marcas/{id_brand}/modelos"
    response = requests.get(formatted_address)
    return response.json()

def years_models_constultation(vehicle_type:str, id_brand:str, id_models:str):
    formatted_address = f"{BASE_URL}/{vehicle_type}/marcas/{id_brand}/modelos/{id_models}/anos"
    response = requests.get(formatted_address)
    return response.json()

def model_year_model_consultation(vehicle_type:str, id_brand:str, id_model:str, id_year:str):
    formatted_adrress = f"{BASE_URL}/{vehicle_type}/marcas/{id_brand}/modelos/{id_model}/anos/{id_year}"
    response = requests.get(formatted_adrress)
    return response.json()
