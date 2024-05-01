from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Skill(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
     
    def get_absolute_url(self):
        return reverse('skill_detail', kwargs={'pk': self.id})

class Application(models.Model):
    STATUS = (
        ('AP', 'Applied'),
        ('IN', 'Interviewing'),
        ('AC', 'Accepted'),
        ('RE', 'Rejected'),
        ('DE', 'Declined')
    )

    job_title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    link = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    date = models.DateField('Date Applied')
    cover_letter_included = models.BooleanField(default=False)
    status = models.CharField(max_length=2, choices=STATUS, default='AP')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    skills = models.ManyToManyField(Skill)


    def __str__(self):
        return f'{self.get_status_display()} '

    def get_absolute_url(self):
        return reverse('detail', kwargs={'application_id': self.id})
    

class Action(models.Model):
    date = models.DateField()
    action = models.CharField(max_length=100)
    application = models.ForeignKey(Application, on_delete=models.CASCADE)

    class Meta:
        ordering = ('-date',)

class Note(models.Model):
    note = models.TextField(max_length=300)
    application = models.ForeignKey(Application, on_delete=models.CASCADE)





