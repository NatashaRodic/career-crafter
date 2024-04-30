# Generated by Django 4.2.11 on 2024-04-30 14:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_action'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='action',
            options={'ordering': ('-date',)},
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.TextField(max_length=300)),
                ('application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.application')),
            ],
        ),
    ]
