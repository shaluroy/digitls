from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    
    return HttpResponse("Welcome in Django Framework")

def aboutus(request):
    return HttpResponse("About us")