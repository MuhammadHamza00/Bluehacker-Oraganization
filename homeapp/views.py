
from sre_constants import SUCCESS
from django.shortcuts import redirect, render, HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from flask import request
from homeapp.models import Contact, newsletter
from homeapp.models import pricing_class
from django.contrib.auth import authenticate 
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth import forms  
from django.shortcuts import redirect, render  
from django.contrib import messages
import django.contrib.auth.models as django_auth_models
django_auth_models.AnonymousUser = User
from django.contrib import messages
from django.urls import reverse_lazy
# from django.views.generic import CreateView
# from homeapp.forms import SignUpForm
from django.shortcuts import render  
from django.contrib.auth.forms import UserCreationForm 


# Create your views here.
def index(request):
    if request.user.is_anonymous==True:
        return redirect('/login')
    if request.method == "POST":
        email1 = request.POST.get('email')
        newsletter1 = newsletter(email=email1)
        newsletter1.save()
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')


def contact(request):
    if request.method == "POST":
        name1 = request.POST.get('name')
        email1 = request.POST.get('email')
        message1 = request.POST.get('message')
        contact1 = Contact(name=name1, email=email1, message=message1)
        contact1.save()
        messages.success(request, 'Message has been sent.!')
    return render(request, 'contact.html')


def defenders(request):
    return render(request, 'defenders.html')


def invader(request):
    return render(request, 'invader.html')


def login(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        print(username,password)
        if user is not None:
            auth_login(request,user)
            return redirect("/")
        else:
            return render(request, 'login.html')
    return render(request, 'login.html')

def logoutuser(request):
    auth_logout(request)
    return redirect('/login')

def pricing(request):
    if request.method=="POST":
        plan=request.POST.get('plan')
        price=request.POST.get('price')
        period=request.POST.get('period')
        pricing1=pricing_class(plan=plan,price=price,period=period)
        pricing1.save()  
    return render(request, 'pricing.html')
    
# class SignUpView(CreateView):
#     form_class = SignUpForm
#     success_url = reverse_lazy('login')
#     template_name = 'signup.html'

def thanks(request):
    return render(request, 'thanks.html')


def signUp(request):
    if request.method == "POST":
        #print(request.POST)
        fm = UserCreationForm(request.POST)
        if fm.is_valid():
            fm.save()
    else:
       fm = UserCreationForm()

    return render(request, 'registration.html', {'form':fm})
        #print(request.POST)
       
# tcalpha beta@2002