import requests
from django.http import JsonResponse
from django.conf import settings

def get_stock_data(request):
    symbol = request.GET.get('symbol', 'AAPL')  # Default to AAPL if no symbol is provided
    api_key = settings.ALPHA_VANTAGE_API_KEY
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}'
    
    response = requests.get(url)
    data = response.json()
    
    return JsonResponse(data)