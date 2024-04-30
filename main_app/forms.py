from django.forms import ModelForm, Select
from .models import Action, Application, Note

class ActionForm(ModelForm):
    class Meta:
        model = Action
        fields = ('date', 'action')

class ApplicationForm(ModelForm):
    class Meta:
        model = Application
        fields = '__all__'
        widgets = {
            'status': Select(choices=Application.STATUS),
        }

class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = '__all__'