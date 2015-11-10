import django
from django.contrib.auth import views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import CreateView
import launchkey
import time
from launchkey_hackathon.settings import BASE_DIR, app, private, secret
from django.contrib.auth import authenticate
import os
from django.core.exceptions import ObjectDoesNotExist


class CreateUser(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('home')
    template_name = 'users/register.html'


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                api = launchkey.API(app_key=app,private_key=private,app_secret=secret)
                user_push_id = True
                session = True
                confirm = api.authorize(username, session, user_push_id)
                while True:
                    response = api.poll_request(confirm)
                    time.sleep(10)
                    if api.is_authorized(confirm, response['auth']):
                        django.contrib.auth.login(request, user)
                        return HttpResponseRedirect(reverse_lazy('home'))
                    else:
                        pass
            else:
                pass
        else:
            raise ObjectDoesNotExist("account does not exist")
    else:
        return views.login(request)


@login_required
def logout(request):
    api = launchkey.API(app_key=app,private_key=private,app_secret=secret)
    api.logout()

