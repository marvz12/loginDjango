from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm


def home(request):
    user = request.user
    return render(request, 'members/home.html', {'user': user})

def userLogin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            messages.success(request, ("Incorrect username or password. Please try again!"))
            return redirect('userLogin')
    else:
        return render(request, 'members/userLogin.html')

def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful. You can now log in.')
            return redirect('profile')
    else:
        form = UserCreationForm()
    
    return render(request, 'members/regForm.html', {'form': form})