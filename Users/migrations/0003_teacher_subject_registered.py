# Generated by Django 3.2.12 on 2022-03-07 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0002_remove_teacher_subject_registered'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher_subject',
            name='registered',
            field=models.DateTimeField(auto_now_add=True, default=1),
            preserve_default=False,
        ),
    ]