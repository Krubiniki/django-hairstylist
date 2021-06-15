import requests
import json

from django.http import HttpResponse, JsonResponse
from .models import Barber

def create_barber_user(request):
    if request.method != 'POST':
        return HttpResponse(status=405)
    try:
        body = json.loads(request.body)
        if 'email' in body: email = body['email']
        if 'password'in body: password = body['password']
        if Barber.objects.filter(email=email).exists():
            return HttpResponse(status=400,content="Já existe uma conta com esse e-mail.")
        Barber.user = Barber.user(email=email)
        Barber.user.set_password(password)
        try:
            Barber.save()
        except Exception as e:
            return HttpResponse(status=400,content="Já existe uma conta com esse e-mail")
        return HttpResponse(status=200,content="Conta criada com sucesso")
    except Exception as e:
        print("Error in create_barber_user: "+str(e))
