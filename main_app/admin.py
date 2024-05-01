from django.contrib import admin
from .models import Application, Action, Note, Skill, Tag

# Register your models here.
admin.site.register([Application, Action, Note, Skill, Tag])