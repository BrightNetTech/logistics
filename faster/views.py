from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def About(request):
    return render(request,'about.html')

def Base(request):
    return render(request,'base.html')

def Blog(request):
    return render(request,'our-blog/blog.html')

def Contact(request):
    return render(request,'contact.html')

def Home(request):
    return render(request,'home.html')

def Price(request):
    return render(request,'price.html')

def Service(request):
    return render(request,'service.html')

def Single(request):
    return render(request,'our-blog/single.html')

def Team(request):
    return render(request,'team.html')

def Tracking(request):
    return render(request,'tracking.html')

def Account(request):
    return render(request,'account.html')

def Thankyou(request):
    return render(request,'thankyou.html')