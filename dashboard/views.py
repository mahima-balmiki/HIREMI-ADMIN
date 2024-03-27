from django.shortcuts import render , HttpResponse
from django.contrib import messages
from .signupform import SignUpForm
from .signinform import SignInForm

#Create your views here.
    
def index(request):
    return render(request,'dashboard/index.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm ( request.POST)
        if form.is_valid():
            # Process the form data
            username = form.cleaned_data['username']
            firstname = form.cleaned_data['firstname']
            lastname = form.cleaned_data['lastname']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            confirmationpassword = form.cleaned_data['confirmationpassword']
            # Do something with the data (save to database, send an email, etc.)
            # Redirect or render success message
    else:
        form = SignUpForm()
    return render(request, 'dashboard/signup.html', {'form': form})

def signin(request):
    if request.method == 'POST':
        form = SignInForm ( request.POST)
        if form.is_valid():
            # Process the form data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
    else:
        form = SignInForm()
    return render(request, 'dashboard/signin.html', {'form': form})

def dashboard(request):
    return render(request,'dashboard/dashboard.html')

def internship(request):
    return render(request,'dashboard/internship.html')

def fresher(request):
    return render(request,'dashboard/fresher.html')

def experience(request):
    return render(request,'dashboard/experience.html')

def mentorship(request):
    return render(request,'dashboard/mentorship.html')

def training(request):
    return render(request,'dashboard/training.html')

def corporate(request):
    return render(request,'dashboard/corporate.html')