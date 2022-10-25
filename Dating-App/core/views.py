from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse(
                       '<h1>Wow Python web development is cool</h1>'
                       '<p> This is a test</p>')