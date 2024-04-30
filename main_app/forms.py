from django.forms import ModelForm, Select
from .models import Action, Application

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