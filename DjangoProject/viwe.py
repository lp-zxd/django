from http.client import HTTPResponse
from tkinter.font import names

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def home(request):
    return render(request,template_name='home.html')
@csrf_exempt
def s_home(request):
    return render(request,template_name='staff_home.html')
def world(request):
    return render(request,template_name="world.html")
def book(request,i):
    return render(request,template_name="book.html",context={"i":i})
def s(request):
    return render(request,template_name="s.html")
def f(request):
    return render(request,template_name="f.html")
