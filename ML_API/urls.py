  
from django.contrib import admin
from django.urls import path
from django.conf.urls import include

from ML_API.views import api_mpg



urlpatterns = [

    path('mpg', api_mpg),
  
]