from django.shortcuts import render, get_object_or_404

from .models import Car, Owner

def detail(request, id):
    car = get_object_or_404(Car, pk=id)
    return render(request, "cars/detail.html", {"car": car})

def owner_list(request):
    return render(request, "cars/list_of_owners.html", {"owner_ob": Owner.objects.all()})

