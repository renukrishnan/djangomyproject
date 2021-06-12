from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def login(request):
    return render(request, "login.html")

def feedback(request):
    return render(request,"feedback.html")

def timetable(request):
    return HttpResponse("<h1> Time Table Here!<h1>")

def leave(request):
    return HttpResponse("<h1> Apply your leave here!<h1>")

def registration(request):
    return render(request,"registration.html")
def home(request):
    return render(request,"index.html")
def get_login(request):
    user_name=request.POST.get("uname")
    password=request.POST.get("pwd")
    print(user_name,password)
    return render(request,"index.html")

