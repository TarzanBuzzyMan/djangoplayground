from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    mylist = {"0", "1", "2", "3", "4", 5, 6, 7, 8}
    return render(request, "home.html", {"var":"string of words", "yy":mylist})


def new_home(request):
    return render(request, "base.html", {"var":"New Home stuff"})

def about(request):
    return render(request, "about.html", {"var":"New Home stuff"})

def contact(request):
    return render(request, "contact.html", {"var":"New Home stuff"})