from django.shortcuts import render
from cars.models import Car
from django.conf import settings
import requests

def index(request):
    return render(request, 'website/index.html',
                  {'cars_ob':Car.objects.all()})


