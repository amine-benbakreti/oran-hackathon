from django.shortcuts import render
from django.http import HttpRequest
# Create your views here.


def view():
    return HttpRequest('hello world')