from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView, CreateView

from .models import SiteStatus
from .forms import  SiteStatusForm


# Create your views here.

class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(*args, *kwargs)
        mylist = {"0", "1", "2", "3", "4", 5, 6, 7, 8}
        context = {"var": "string of words", "yy": mylist}
        return context


class AboutView(TemplateView):
    template_name = "about.html"


class ContactView(TemplateView):
    template_name = "contact.html"


class SiteStatusView(CreateView):
    form_class = SiteStatusForm
    template_name = "sitestatus_form.html"
