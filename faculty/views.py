from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def loginpage(request):
    return HttpResponse("<h1> Welcome to login page</h1>")

def feedbacks(request):
    return HttpResponse("<h1> View Feedback Here!<h1>")

def addtimetable(request):
    return HttpResponse("<h1> Time Table Here!<h1>")

def syllabus(request):
    return HttpResponse("<h1> Post Syllabus here!<h1>")