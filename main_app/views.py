from django.shortcuts import render, redirect
from .models import Application, Skill, Tag
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .forms import ActionForm, ApplicationForm, NoteForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin




# Create your views here.

def home (request):
    return render (request, 'home.html')

def about (request):
    return render(request, 'about.html')

@login_required
def applications_index (request):
    applications = Application.objects.filter(user=request.user)
    return render(request, 'applications/index.html', {
        'applications': applications
    })

@login_required
def applications_detail (request, application_id):
    application = Application.objects.get(id=application_id)
    id_list = application.skills.all().values_list('id')
    skills_that_application_doesnt_have = Skill.objects.exclude(id__in = id_list)
    id_list2 = application.tags.all().values_list('id')
    tags_that_application_doesnt_have = Tag.objects.exclude(id__in = id_list2)


    action_form = ActionForm()
    return render(request, 'applications/detail.html', {
        'application': application,
        'action_form': action_form,
        'skills': skills_that_application_doesnt_have,
        'tags': tags_that_application_doesnt_have
    })

def assoc_skill(request, application_id, skill_id):
  Application.objects.get(id=application_id).skills.add(skill_id)
  return redirect('detail', application_id=application_id)

def assoc_tag(request, application_id, tag_id):
  Application.objects.get(id=application_id).tags.add(tag_id)
  return redirect('detail', application_id=application_id)

@login_required
def add_action(request, application_id):
  form = ActionForm(request.POST)
  if form.is_valid():
    new_action = form.save(commit=False)
    new_action.application_id = application_id
    new_action.save()
  return redirect('detail', application_id=application_id)

@login_required
def add_note(request, application_id):
    form = NoteForm(request.POST)
    if form.is_valid():
        new_note = form.save(commit=False)
        new_note.application_id = application_id
        new_note.save()
    return redirect('detail', application_id=application_id)


class ApplicationCreate(LoginRequiredMixin, CreateView):
    form_class = ApplicationForm
    model = Application

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ApplicationUpdate(LoginRequiredMixin, UpdateView):
    model = Application
    fields = ('status',)

class ApplicationDelete(LoginRequiredMixin, DeleteView):
    model = Application
    success_url = '/applications/'


def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

class SkillList(ListView):
  model = Skill

class SkillCreate(CreateView):
  model = Skill
  fields = '__all__'
  success_url = '/applications/'

class SkillDelete(DeleteView):
  model = Skill
  success_url = '/skills'

class SkillDetail(DetailView):
  model = Skill

class TagCreate(CreateView):
  model = Tag
  fields = '__all__'
  success_url = '/applications/'