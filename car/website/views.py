from django.shortcuts import render
from cars.models import Car


def welcome(request):
    return render(request, 'website/welcome.html',
                  {'cars_ob':Car.objects.all()})
