from django.conf.urls import url, include
from .views import *
from django.contrib.staticfiles import views
from django.urls import re_path
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'', login_required(index), name='index'),
]