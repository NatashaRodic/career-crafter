from django.contrib import admin
from .models import Application, Action

# Register your models here.
admin.site.register([Application, Action])