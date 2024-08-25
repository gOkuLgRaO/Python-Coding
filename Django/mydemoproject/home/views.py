# from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse("<h1>Hey I am a Django server</h1>")

def success_page(request):
    return HttpResponse("<h1> Hey this is a success page</h1>")