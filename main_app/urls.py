from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('applications/', views.applications_index, name='index'),
    path('applications/<int:application_id>/', views.applications_detail, name='detail'),
    path('applications/create/', views.ApplicationCreate.as_view(), name='application_create'),
    path('applications/<int:pk>/update', views.ApplicationUpdate.as_view(), name='application_update'),
    path('applications/<int:pk>/delete', views.ApplicationDelete.as_view(), name='application_delete'),
    path('applications/<int:application_id>/add_action/', views.add_action, name='add_action'),
    path('applications/<int:application_id>/add_note/', views.add_note, name='add_note'),
    path('accounts/signup/', views.signup, name='signup'),
]