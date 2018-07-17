from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    ht = """<!DOCTYPE html>
    <html lang=en>
    <head>
    </head>
    <body>
    <h1>Hello!</h1>
    <p>My HTML </p>
    </body>
    </html>
    """
    return HttpResponse(ht)

def home(request):
    return render(request,"Homepage")

def mything(request):
    return "Oscar"
