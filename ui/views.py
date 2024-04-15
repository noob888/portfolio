from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class home_view(TemplateView):
    template_name = 'index.html'

class about_view(TemplateView):
    template_name = 'about.html'

class contact_view(TemplateView):
    template_name = 'contact.html'


class projects_view(TemplateView):
    template_name = 'projects.html'

class services_view(TemplateView):
    template_name = 'services.html'

class single_page_view(TemplateView):
    template_name = 'single-page.html'



