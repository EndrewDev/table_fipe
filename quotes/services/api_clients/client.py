import requests

BASE_URL = "https://parallelum.com.br/fipe/api/v1"

def consult_marcas(tipo_veiculo:str):
    formatted_address = f'{BASE_URL}/{tipo_veiculo}/marcas'
    response = requests.get(formatted_address)
    return response.json()