# Generated by Django 4.2.11 on 2024-05-01 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='tags',
            field=models.ManyToManyField(to='main_app.tag'),
        ),
    ]