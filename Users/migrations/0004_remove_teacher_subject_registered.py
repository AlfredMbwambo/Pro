# Generated by Django 3.2.12 on 2022-03-07 19:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0003_teacher_subject_registered'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher_subject',
            name='registered',
        ),
    ]
