from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('applications/', views.applications_index, name='index')
]