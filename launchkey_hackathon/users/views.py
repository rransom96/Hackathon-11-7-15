import os
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.template.context_processors import request
from django.views.generic import View
import launchkey
from launchkey_hackathon.settings import BASE_DIR


class Login(request):
    username = request.POST['username']
    password = request.POST['password']
    app = '4910033767'
    secret = '8p20rbc2urf9f9h4wgn6hzarp0wvc7zb'
    private = open(os.path.join(BASE_DIR, 'secret_key', 'private_key'), 'r').read()
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            confirm = launchkey.API(app_key=app,private_key=private,app_secret=secret)
            if confirm:
                login(request, user)
            else:
                pass
        else:
            pass
    else:
        raise ObjectDoesNotExist("account does not exist")

