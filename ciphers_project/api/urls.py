from urllib import request
from django.urls import path
from .views import greetings, encode


urlpatterns = [
    path('',greetings),
    path('cipherfunc/<str:plain_text>/<int:shift>',encode)
]
