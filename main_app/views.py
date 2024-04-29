from django.shortcuts import render
from .models import Application
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import ActionForm


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
    action_form = ActionForm()
    return render(request, 'applications/detail.html', {
        'application': application,
        'action_form': action_form
    })

class ApplicationCreate(CreateView):
    model = Application
    fields = ['job_title', 'company', 'link', 'location', 'date', 'cover_letter_included', 'status']


class ApplicationUpdate(UpdateView):
    model = Application
    fields = ('status',)

class ApplicationDelete(DeleteView):
    model = Application
    success_url = '/applications/'