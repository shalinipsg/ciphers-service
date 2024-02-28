from urllib import request
from django.urls import path
from .views import greetings, encode


urlpatterns = [
    path('',greetings),
    path('cipher_func/<str:plain_text>/<int:shift>',encode)
]
