from django.shortcuts import render, redirect
from .models import Application
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import ActionForm, ApplicationForm, NoteForm


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

def add_action(request, application_id):
  form = ActionForm(request.POST)
  if form.is_valid():
    new_action = form.save(commit=False)
    new_action.application_id = application_id
    new_action.save()
  return redirect('detail', application_id=application_id)

def add_note(request, application_id):
    form = NoteForm(request.POST)
    if form.is_valid():
        new_note = form.save(commit=False)
        new_note.application_id = application_id
        new_note.save()
    return redirect('detail', application_id=application_id)


class ApplicationCreate(CreateView):
    form_class = ApplicationForm
    model = Application
    # fields = ['job_title', 'company', 'link', 'location', 'date', 'cover_letter_included', 'status']


class ApplicationUpdate(UpdateView):
    model = Application
    fields = ('status',)

class ApplicationDelete(DeleteView):
    model = Application
    success_url = '/applications/'