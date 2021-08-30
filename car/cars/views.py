from django.shortcuts import render, get_object_or_404, redirect
from .models import Car, Owner
from .forms import CarForm, CreateUserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages



def detail(request, id):
    car = get_object_or_404(Car, pk=id)
    return render(request, "cars/detail.html", {"car": car})

def owner_list(request):
    return render(request, "cars/list_of_owners.html", {"owner_ob": Owner.objects.all()})


@login_required(login_url='login')
def new(request):
    if request.method == "POST":
        form = CarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("welcome")
    else:
        form = CarForm()
    return render(request, "cars/new.html", {"form": form})


def about(request):
    return render(request, "cars/about.html")


def owner_cars(request, id):
    #o_cars = Car.objects.get(owner=id)
    o_cars = get_object_or_404(Car, owner=id)
    return render(request, "cars/owner_cars.html", {"o_cars": o_cars})



def registerPage(request):
    if request.user.is_authenticated :
        return redirect('welcome')
    else:

        form = CreateUserForm()

        if request.method == "POST":
            form = CreateUserForm(request.POST)

            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, user+", Successfully registered!" )
                return redirect('login')

        context = {'form': form}
        return render(request, "cars/register.html", context)



def loginPage(request):
    if request.user.is_authenticated:
        return redirect('welcome')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password )
            if user is not None:   # if user authenticate
                login(request, user)
                return redirect('welcome')
            else:
                messages.info(request, 'Username/Password is incorrect!')


        context = {}
        return render(request, "cars/login.html", context)


def logoutUser(request):
    logout(request)
    return redirect('login')





























