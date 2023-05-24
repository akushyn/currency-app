import datetime
import requests
from django.utils import timezone

from currency.models import ExchangeRateProvider, ExchangeRate


class ProviderService(object):
    def __init__(self, name, api_url):
        self.name = name
        self.api_url = api_url

    def get_or_create(self):
        provider, created = ExchangeRateProvider.objects.get_or_create(name=self.name, api_url=self.api_url)
        if created:
            # The provider was created because it didn't exist
            print("ExchangeRateProvider created:", provider)
        else:
            # The provider already exists
            print("Existing ExchangeRateProvider retrieved:", provider)

        return provider


class ExchangeRatesService:

    CURRENCIES = ['GBP', 'USD', 'CHF', 'EUR']

    def __init__(self, provider, start_date, end_date):
        self.provider = provider
        self.start_date = start_date
        self.end_date = end_date

    @property
    def url(self):
        return self.provider.api_url

    def get_rates(self):
        delta = datetime.timedelta(days=1)
        current = self.start_date

        while current < self.end_date:
            currency_rates = self.get_rate(date=current)
            print(currency_rates)
            for rates in currency_rates:
                rates['provider_id'] = self.provider.pk
                ExchangeRate.objects.get_or_create(**rates)
            current += delta

    def get_rate(self, date):
        params = {
            "date": str(date.strftime('%d.%m.%Y'))
        }

        response = requests.get(self.url, params=params)
        data = response.json()

        rates = data['exchangeRate']
        currency_rates = []
        base_currency = data['baseCurrencyLit']

        for r in rates:
            if r['currency'] not in self.CURRENCIES:
                continue

            currency_rates.append(
                {
                    'base_currency': base_currency,
                    'currency': r['currency'],
                    'date': timezone.make_aware(date),
                    'sale_rate': r['saleRate'],
                    'buy_rate': r['purchaseRate']
                }
            )

        return currency_rates
