from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from cars.models import Car

def welcome(request):
    return render(request, 'website/welcome.html',
                  {'cars_ob':Car.objects.all()})

def date(request):
    return HttpResponse('This page was served at' + str(datetime.now()))


def about(request):
    return HttpResponse('This page was build by Ammar on August 12, 2021 ' )

