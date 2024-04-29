from django.db import models
from django.urls import reverse

# Create your models here.

class Application(models.Model):
    job_title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    link = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    date = models.DateField('Date Applied')
    cover_letter_included = models.BooleanField(default=False)

    STATUS = (
        ('AP', 'Applied'),
        ('IN', 'Interviewing'),
        ('AC', 'Accepted'),
        ('RE', 'Rejected'),
        ('DE', 'Declined')
    )

    status = models.CharField(max_length=2, choices=STATUS, default='AP')

    def get_absolute_url(self):
        return reverse('detail', kwargs={'application_id': self.id})


