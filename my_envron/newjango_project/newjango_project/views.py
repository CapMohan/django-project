from django.shortcuts import render
from django.http import HttpResponse


def demo(request):
    return HttpResponse("Welcome to new django project to build application")