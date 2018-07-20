from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView

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


class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(*args, *kwargs)

class AboutView(TemplateView):
    template_name = "about.html"

class ContactView(TemplateView):
    template_name = "contact.html"