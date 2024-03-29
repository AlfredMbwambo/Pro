# Generated by Django 3.2.12 on 2022-03-08 11:25

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0005_auto_20220307_2059'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='teacher_subject',
            managers=[
                ('teacher_subjects', django.db.models.manager.Manager()),
            ],
        ),
        migrations.RenameField(
            model_name='teacher_subject',
            old_name='teach_id',
            new_name='subject_teacher_id',
        ),
        migrations.AlterModelTable(
            name='teacher_subject',
            table='teacher_subjects',
        ),
    ]
