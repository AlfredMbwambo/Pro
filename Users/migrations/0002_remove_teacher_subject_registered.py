# Generated by Django 3.2.12 on 2022-03-07 18:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher_subject',
            name='registered',
        ),
    ]