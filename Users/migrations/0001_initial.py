# Generated by Django 3.2.12 on 2022-03-04 13:38

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exam_type',
            fields=[
                ('exam_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('exam_name', models.CharField(max_length=150)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modifield_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'examtypes',
            },
            managers=[
                ('examtypes', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Stream',
            fields=[
                ('stream_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('stream_name', models.CharField(max_length=150)),
                ('registered', models.DateTimeField(auto_now_add=True)),
                ('modifield_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'streams',
            },
            managers=[
                ('streams', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('middle_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('standard', models.CharField(max_length=50)),
                ('registration_number', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=150)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modifield_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'students',
            },
            managers=[
                ('students', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('subject_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('subject_name', models.CharField(max_length=150)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modifield_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'subjects',
            },
            managers=[
                ('subjects', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('teacher_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('teacher_name', models.CharField(max_length=150)),
                ('phone_number', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=150)),
                ('password', models.CharField(max_length=150)),
                ('registered', models.DateTimeField(auto_now_add=True)),
                ('modifield_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'teachers',
            },
            managers=[
                ('teachers', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Year',
            fields=[
                ('year_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('year_name', models.IntegerField(verbose_name=150)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modifield_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'years',
            },
            managers=[
                ('years', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Teacher_subject',
            fields=[
                ('subject_teacher_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('registered', models.DateTimeField(auto_now_add=True)),
                ('modifield_at', models.DateTimeField(auto_now=True)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Users.subject')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Users.teacher')),
            ],
            options={
                'db_table': 'teacher_subjects',
            },
            managers=[
                ('teacher_subject', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('result_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('score', models.IntegerField(verbose_name=50)),
                ('grade', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modifield_at', models.DateTimeField(auto_now=True)),
                ('examtype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Users.exam_type')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Users.student')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Users.subject')),
                ('year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Users.year')),
            ],
            options={
                'db_table': 'results',
            },
            managers=[
                ('results', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Darasa',
            fields=[
                ('class_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('class_name', models.CharField(max_length=150)),
                ('registered', models.DateTimeField(auto_now_add=True)),
                ('modifield_at', models.DateTimeField(auto_now=True)),
                ('stream', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Users.stream')),
            ],
            options={
                'db_table': 'classes',
            },
            managers=[
                ('classes', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Class_subject',
            fields=[
                ('class_subject_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('darasa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Users.darasa')),
                ('teacher_subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Users.teacher_subject')),
            ],
            options={
                'db_table': 'class_subjects',
            },
            managers=[
                ('class_subjects', django.db.models.manager.Manager()),
            ],
        ),
    ]
