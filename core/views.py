import datetime

from django.shortcuts import render
from currency.services import ExchangeRatesService, ProviderService


def index(request):

    provider_data = dict(
        name='privat24',
        url='https://api.privatbank.ua/p24api/exchange_rates'
    )

    provider_service = ProviderService(
        name=provider_data.get('name'),
        api_url=provider_data.get('url')
    )
    service = ExchangeRatesService(
        provider=provider_service.get_or_create(),
        start_date=datetime.datetime(2023, 5, 1),
        end_date=datetime.datetime.now()
    )

    rates = service.get_rates()
    print(rates)
    return render(request, 'core/index.html')
