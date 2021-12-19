from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(Request,a):
    return HttpResponse("This is index"+str(a))