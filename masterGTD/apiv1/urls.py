from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
from .views import *

urlpatterns = [
    url(r'^$', index),
]