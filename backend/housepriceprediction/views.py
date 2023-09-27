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
        else:
            my_user = User.objects.create_user(username, email, password1)
            my_user.save()
            return redirect('/page/login/')
    return render(request,'signup/signup.html')

def error(request):
    return render(request,'404.html')



# def make_prediction(form_data):
#     # Add your prediction logic here
#     # For demonstration purposes, let's assume a fixed prediction value
#     return 100000


def prediction(request):
    if request.method == 'POST':
        # Get form data from the request
        location = request.POST.get('location')
        bedroom = int(request.POST.get('bedroom'))
        city = request.POST.get('city')
        floors = int(request.POST.get('floors'))
        bathroom = int(request.POST.get('bathroom'))
        parking = int(request.POST.get('parking'))
        house_face = request.POST.get('face')
        # Extract amenities as a list of selected values
        amenities = request.POST.getlist('amenities')
        road_type = request.POST.get('roadtype')

        # Perform validation if needed

        # Call your prediction function to get the predicted value
        # prediction_value = make_prediction(request.POST)
        prediction_value = 19999

        # Render the result template and pass the prediction value to the template context
        return render(request, 'result/result.html', {'prediction': prediction_value})

    return render(request, 'prediction/prediction.html')

def result(request):
    # Retrieve the prediction value from the URL parameter
    prediction_value = request.GET.get('prediction')

    # Render the result page and pass the prediction value to the template
    return render(request, 'result/result.html', {'prediction': prediction_value})