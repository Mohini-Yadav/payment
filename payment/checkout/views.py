from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
import os
import Adyen

adyen = Adyen.Adyen()
adyen.payment.client.platform = "test"
adyen.client.xapikey = 'AQEyhmfxLI3MaBFLw0m/n3Q5qf3VaY9UCJ14XWZE03G/k2NFitRvbe4N1XqH1eHaH2AksaEQwV1bDb7kfNy1WIxIIkxgBw==-y3qzswmlmALhxaVPNjYf74bqPotG12HroatrKA066yE=-W+t7NF;s4}%=kUSD'
# Create your views here.
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def checkout_view(request):
    # return HttpResponse("<h1>checkout_page</h1>")

    #
    return render(request, "checkout.html", {})


def home_view(request):
    # return HttpResponse("<h1>checkout_page</h1>")
    return render(request, "home.html", {})


@csrf_exempt
def response_view(request):

    # return HttpResponse("<h1>checkout_page</h1>")
    country_code = request.POST.get('Country Code')
    currency = request.POST.get('Currency')
    value = request.POST.get('Amount')
    channel = request.POST.get('Channel')
    shopperlocale = request.POST.get('shopperLocale')
    print("RRRRRRRRRRRRRRR ",country_code,currency,value,channel,shopperlocale)
    payload = {

        'merchantAccount': 'AdyenRecruitmentCOM',
        'countryCode': country_code,
        'shopperLocale': shopperlocale,
        'amount': {
            'value': value,
            'currency': currency
        },
        'channel': channel

    }
    response = adyen.checkout.payment_methods(payload)
    print(response)
    return render(response, "response.html", {})
