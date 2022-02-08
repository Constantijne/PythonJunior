from django.shortcuts import render
from django.http import HttpResponse


def index(requests):
    return HttpResponse('Hello. It`s ToDo App!)')
# Create your views here.
