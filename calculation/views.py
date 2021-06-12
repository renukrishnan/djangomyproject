from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request,"calhome.html")
def add(request):
    return render(request,"addition.html")
def sub(request):
    return render(request,"subtraction.html")
def mul(request):
    return render(request,"multiplication.html")
def div(request):
    return render(request,"division.html")
def get_add(request):
    first_number=request.POST.get("num1")
    second_number=request.POST.get("num2")
    result=int(first_number)+int(second_number)
    print("Sum of numbers is:",result)
    #return render(request,"calhome.html")
    #to send data from backend to front end-> is only possible in dictionary format->{"key":value"}
    context={}
    context["res"]=result#context={"res":3)->3 is the resultvalue(2+1)=3}
    return render(request,"addition.html",context)
def get_sub(request):
    first_number=request.POST.get("num1")
    second_number=request.POST.get("num2")
    result=int(first_number)-int(second_number)
    print("Sub of numbers is:",result)
    #return render(request,"calhome.html")
    context={}
    context["res"]=result
    return render(request,"subtraction.html",context)
def get_mul(request):
    first_number=request.POST.get("num1")
    second_number=request.POST.get("num2")
    result=int(first_number)*int(second_number)
    print("Multilpication of numbers is:",result)
    #return render(request,"calhome.html")
    context = {}
    context["res"] = result
    return render(request, "multiplication.html", context)
def get_div(request):
    first_number=request.POST.get("num1")
    second_number=request.POST.get("num2")
    result=int(first_number)/int(second_number)
    print("Sum of numbers is:",result)
   # return render(request,"calhome.html")
    context = {}
    context["res"] = result
    return render(request, "division.html", context)
