from django.shortcuts import render
from django.http import JsonResponse
from .ciphers import ciphers_fun
# Create your views here.
def greetings(request):
    result={'message':'Greetings from cipher service'}
    return JsonResponse(result)

def encode(request):
    print("nfdm,")
    parameters=dict(request.GET)
    print("print params",parameters)
    cipher=ciphers_fun(plain_text,shift)
    return JsonResponse({'ciphered text':cipher})
    