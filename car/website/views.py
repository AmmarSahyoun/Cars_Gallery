from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


def welcome(request):
    return HttpResponse('Welcome to the Gallery')

def date(request):
    return HttpResponse('This page was served at' + str(datetime.now()))


def about(request):
    return HttpResponse('This page was build by Ammar on August 12, 2021 ' )