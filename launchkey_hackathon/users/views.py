
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.contrib.auth.models import User
from users.forms import UserCreateForm
from django.views.generic import CreateView
import launchkey
from launchkey_hackathon.settings import BASE_DIR
from django.contrib.auth import authenticate, login
# from django.template.context_processors import request
import os
from django.core.exceptions import ObjectDoesNotExist



class CreateUser(CreateView):

    model = User
    form_class = UserCreateForm
    success_url = reverse_lazy('home')
    template_name = 'users/register.html'


def Login(request):
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


