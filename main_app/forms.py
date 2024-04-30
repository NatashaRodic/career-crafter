from django.forms import ModelForm, Select
from .models import Action, Application, Note

class ActionForm(ModelForm):
    class Meta:
        model = Action
        fields = ('date', 'action')

class ApplicationForm(ModelForm):
    class Meta:
        model = Application
        fields = ('job_title', 'company', 'link', 'location', 'date', 'cover_letter_included', 'status')
        widgets = {
            'status': Select(choices=Application.STATUS),
        }

class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = '__all__'