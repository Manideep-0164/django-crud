from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def basic_home(request):
    return HttpResponse("Welcome to homepage!")

def greet_user(requset,username):
    return HttpResponse("Hello, "+username+"!")

def farewell_user(request,username):
    return HttpResponse("Goodbye, "+username+"!")