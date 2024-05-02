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
    path('skills/', views.SkillList.as_view(), name='skills_index'),
    path('skills/<int:pk>/', views.SkillDetail.as_view(), name='skills_detail'),
    path('skills/create', views.SkillCreate.as_view(), name='skills_create'),
    path('applications/<int:application_id>/assoc_skill/<int:skill_id>/', views.assoc_skill, name='assoc_skill'),
    path('tags/create', views.TagCreate.as_view(), name='tags_create'),
    path('applications/<int:application_id>/assoc_tag/<int:tag_id>/', views.assoc_tag, name='assoc_tag'),
]