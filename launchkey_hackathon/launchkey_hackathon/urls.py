"""launchkey_hackathon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from users.views import CreateUser
from hackathon_app.views import WelcomePage, ListPosts, CreatePost

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^logout/', 'django.contrib.auth.views.logout', {'next_page': "/"}, name='logout'),
    url(r'^login/$', 'users.views.Login', name='login'),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^register/', CreateUser.as_view(), name='register'),
    url(r'^$', WelcomePage.as_view(), name="home" ),
    url(r'^posts/', ListPosts.as_view(), name="posts"),
    url(r'^create/$', login_required(CreatePost.as_view()), name='post_create'),
]
