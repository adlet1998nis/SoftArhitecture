import requests
from django.shortcuts import render

from . import constants as const


def hello(request):
    context = {}

    resp = requests.get(url=f'{const.BACKEND_API_URL}/get-name')
    name_data = resp.json()
    context.update(name_data)

    resp = requests.get(url=f'{const.BACKEND_API_URL}/get-surname')
    surname_data = resp.json()
    context.update(surname_data)

    resp = requests.get(url=f'{const.BACKEND_API_URL}/get-id')
    id_data = resp.json()
    context.update(id_data)

    resp = requests.get(url=f'{const.BACKEND_API_URL}/get-additional-message')
    msg_data = resp.json()
    context.update(msg_data)

    return render(request, 'index.html', context)
