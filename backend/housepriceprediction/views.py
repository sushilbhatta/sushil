# from django.contrib.auth import login, authenticate
# from django.contrib import messages
# from django.shortcuts import render, redirect
# from django.contrib.auth.models import User
# from django.contrib.auth import authenticate, login as auth_login
# from django.http import HttpResponse
# from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout


# Create your views here.

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about/About.html')

def contact(request):
    return render(request,'contact/contact.html')

# def login(request):
    # if request.method == 'POST':
    #     username = request.POST.get('username')
    #     password = request.POST.get('password')

    #     username = authenticate(request, username=username, password=password)
    #     if username is not None:
    #         login(request, username)
    #         return redirect('home')
    #     else:
    #         return HttpResponse('Error, user does not exist')
    # return render(request,'login/login.html', {})
def login(request):
    if request.method == 'POST':
            username = request.POST.get('username')
            password1 = request.POST.get('password')

            user = authenticate(request, username=username, password=password1)
            if user is not None:
                auth_login(request, user)
                return redirect('/page/home/')
            else:
                return HttpResponse('Error, user does not exist or incorrect password.')

    return render(request, 'login/login.html')


def custom_logout(request):
    auth_logout(request)
    return redirect('/page/login/')


@login_required
def prediction(request):
    return render(request,'prediction/prediction.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password')
        password2 = request.POST.get('confirm_pass')

        if password1 != password2:
            messages.error(
                request, "Passwords do not match. Please try again.")
            return redirect('signup')

        # Check if the username is already taken
        elif User.objects.filter(username=username).exists():
            messages.error(
                request, "Username is already taken. Please choose a different one.")
            return redirect('signup')

        # Check if the email is already in use
        elif User.objects.filter(email=email).exists():
            messages.error(
                request, "Email is already in use. Please use a different email.")
            return redirect('signup')

        # Create the user
          # Check if the username is already taken
        #
        else:

            my_user = User.objects.create_user(username, email, password1)
            my_user.save()
            return redirect('/page/login/')


        # # Log the user in
        # user = authenticate(request, username=username, password=password1)
        # if user is not None:
        #     login(request, user)

        # messages.success(
            # request, "Registration successful. You are now logged in.")
        # return redirect('/page/login/')


    return render(request,'signup/signup.html')

def error(request):
    return render(request,'404.html')
