import time
from django.core.mail import send_mail
from django.shortcuts import render

from currency.tasks import add
from django.conf import settings


def send_custom_email():

    recipients = ['fifand1005@gmail.com']
    send_mail(
        subject='subject',
        message='test message',
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=recipients
    )


def index(request):

    result = add.delay(5, 7)
    print(result.status)
    send_custom_email()

    print('done')
    # provider_data = dict(
    #     name='privat24',
    #     url='https://api.privatbank.ua/p24api/exchange_rates'
    # )
    #
    # provider_service = ProviderService(
    #     name=provider_data.get('name'),
    #     api_url=provider_data.get('url')
    # )
    # service = ExchangeRatesService(
    #     provider=provider_service.get_or_create(),
    #     start_date=datetime.datetime(2023, 5, 1),
    #     end_date=datetime.datetime.now()
    # )
    #
    # rates = service.get_rates()
    # print(rates)
    return render(request, 'core/index.html')
