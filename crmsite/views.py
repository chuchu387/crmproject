from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.
def home(request):
    # check to see if logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        #authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been Logged In!")
            return redirect('home')
        else:
            messages.success(request, "there was an error in log in!, please try again")
    else:
        return render(request, 'home.html', {})
    return render(request, 'home.html', {})





def logout_user(request):
    logout(request)
    messages.success(request, "you have been loged out...")
    return render(request, 'home.html', {})

def register_user(request):
    return render(request, 'register.html', {})