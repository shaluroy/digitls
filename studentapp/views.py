from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return render(request,"studentapp/index.html")
def addition(request):
    a=100
    b=200
    c=a+b
    return HttpResponse("Result is "+str(c))
