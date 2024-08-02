from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse

def signup_view(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']

        # Create user
        user = User.objects.create_user(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            email=email
        )

        # Authenticate and login the user
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  

        return HttpResponse("User creation failed.")
    else:
        return render(request, './registration/signup.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  
        else:
            return HttpResponse("Invalid login credentials")
    else:
        return render(request, './registration/login.html')

def logout_view(request):
    logout(request)
    return redirect('index')


def header(request):
    return render(request, 'base.html')
