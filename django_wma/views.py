from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("A list of all the available water resources")
