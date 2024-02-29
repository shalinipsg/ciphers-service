from django.shortcuts import render
from django.http import JsonResponse
from .ciphers import ciphers_fun
# Create your views here.
def greetings(request):
    result={'message':'Greetings from cipher service'}
    return JsonResponse(result)

def encode(request,plain_text,shift):
    print("nfdm,")
    parameters=dict(request.GET)
    print("print params",parameters,plain_text,shift)
    cipher=ciphers_fun(plain_text,shift)
    return JsonResponse({'ciphered text':cipher})
    