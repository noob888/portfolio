from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import ContactPageForm, HomePageForm

# Create your views here.

def home_view(request):
    template = 'index.html'

    if request.method == 'POST':
        form = HomePageForm(request.POST)
        if form.is_valid():
           form.save()
    else:
        form = HomePageForm()

    context ={'form': form}

    return render(request, template, context)

def about_view(request):
    template = 'about.html'

    if request.method == 'POST':
        form = HomePageForm(request.POST)
        if form.is_valid():
           form.save()
    else:
        form = HomePageForm()

    context ={'form': form}

    return render(request, template, context)

def contact_view(request):
    template = 'contact.html'

    if request.method == 'POST':
        contact_form = ContactPageForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
        form = HomePageForm(request.POST)
        if form.is_valid():
           form.save()
    else:
        contact_form = ContactPageForm()
        form = HomePageForm()

    context ={
        'contact_form': contact_form,
        'form': form}

    return render(request, template, context)


class projects_view(TemplateView):
    template_name = 'projects.html'

class services_view(TemplateView):
    template_name = 'services.html'

class single_page_view(TemplateView):
    template_name = 'single-page.html'





