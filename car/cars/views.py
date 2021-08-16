from django.shortcuts import render, get_object_or_404, redirect
from .models import Car, Owner
from django.http import HttpResponse
from .forms import MeetingForm

def detail(request, id):
    car = get_object_or_404(Car, pk=id)
    return render(request, "cars/detail.html", {"car": car})

def owner_list(request):
    return render(request, "cars/list_of_owners.html", {"owner_ob": Owner.objects.all()})



def new(request):
    if request.method == "POST":
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("welcome")
    else:
        form = MeetingForm()
    return render(request, "cars/new.html", {"form": form})


def about(request):
    return render(request, "cars/about.html")
