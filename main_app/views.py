from django.shortcuts import render
from .models import Application


# Create your views here.

def home (request):
    return render (request, 'home.html')

def about (request):
    return render(request, 'about.html')

def applications_index (request):
    applications = Application.objects.all()
    return render(request, 'applications/index.html', {
        'applications': applications
    })

def applications_detail (request, application_id):
    application = Application.objects.get(id=application_id)
    return render(request, 'applications/detail.html', {
        'application': application
    })