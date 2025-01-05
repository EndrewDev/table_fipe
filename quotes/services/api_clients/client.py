import requests

BASE_URL = "https://parallelum.com.br/fipe/api/v1"

def brand_consultation(vehicle_type:str):
    formatted_address = f'{BASE_URL}/{vehicle_type}/brand'
    response = requests.get(formatted_address)
    return response.json()