from django.shortcuts import render

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http.response import json

from Users.user_logic import admin_login
from Users.user_logic import teacher_registration
from Users.user_logic import teacher_login
from Users.user_logic import password_recovery
from Users.user_logic import subject_registration
from Users.user_logic import darasa
from Users.user_logic import stream


@csrf_exempt
def API(request):
    response = ""
    if request.method == "POST":
        client_request = request.body
        client_data = json.loads(client_request)

        if client_data['code'] == 100:
            response = admin_login(client_data['data'])

        if client_data['code'] == 101:
            response = teacher_registration(client_data['data'])

        if client_data['code'] == 102:
            response = teacher_login(client_data['data'])

        if client_data['code'] == 103:
            response = password_recovery(client_data['data'])

        if client_data['code'] == 104:
            response = subject_registration(client_data['data'])

        if client_data['code'] == 105:
            response = stream(client_data['data'])

        if client_data['code'] == 106:
            response = darasa(client_data['data'])



    return HttpResponse(response)