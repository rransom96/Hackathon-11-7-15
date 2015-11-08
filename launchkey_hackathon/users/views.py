from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
import time
from users.forms import UserCreateForm
from django.views.generic import CreateView
import launchkey
from launchkey_hackathon.settings import BASE_DIR
from django.contrib.auth import authenticate, login
import os
from django.core.exceptions import ObjectDoesNotExist



class CreateUser(CreateView):

    model = User
    form_class = UserCreateForm
    success_url = reverse_lazy('home')
    template_name = 'users/register.html'


def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        app = '4910033767'
        secret = '8p20rbc2urf9f9h4wgn6hzarp0wvc7zb'
        private = open(os.path.join(BASE_DIR, 'secret_key', 'private_key'), 'r').read()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                api = launchkey.API(app_key=app,private_key=private,app_secret=secret)
                confirm = api.authorize(user)
                while True:
                    response = api.poll_request(confirm)
                    time.sleep(90)
                    if api.is_authorized(confirm, response['auth']):
                        login(request, user)
                        break
                    else:
                        pass
            else:
                pass
        else:
            raise ObjectDoesNotExist("account does not exist")
    else:
        return render(request, template_name='registration/login.html')
