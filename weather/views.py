from django.shortcuts import render
from .models import Address
import requests as req



WEATHER_API = '9e05111581b779f9c85b5a9d9629afe1'

# Create your views here.
def address_list(request):
    addresses = Address.objects.all()
    data = {
        'all_addresses': [],
    }
    for address in addresses:
        data['all_addresses'].append({
            'address': address,
            'temp': _get_weather(address.zip_code)
            })
    print(data)
    return render(request, 'weather/address_list.html', data)

def _get_weather(zip_code):
    url = f'https://api.openweathermap.org/data/2.5/weather?zip={zip_code},us&appid={WEATHER_API}&units=imperial'
    response = req.get(url)
    res_data = response.json()
    return res_data['main']['temp']
