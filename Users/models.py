from django.db import models

from django.db import models


class Teacher(models.Model):
    teacher_id = models.CharField(max_length=50, primary_key=True)
    teacher_name = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=50)
    email = models.CharField(max_length=150)
    password = models.CharField(max_length=150)
    registered = models.DateTimeField(auto_now_add=True)
    modifield_at = models.DateTimeField(auto_now=True)

    teachers = models.Manager()

    class Meta:
        db_table = "teachers"

class Subject(models.Model):
    subject_id = models.CharField(max_length=50, primary_key=True)
    subject_name = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    modifield_at = models.DateTimeField(auto_now=True)

    subjects = models.Manager()

    class Meta:
        db_table = "subjects"

class Teacher_subject(models.Model):
    subject_teacher_id = models.CharField(max_length=50, primary_key=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    modifield_at = models.DateTimeField(auto_now=True)

    teacher_subjects = models.Manager()

    class Meta:
        db_table = "teacher_subjects"

class Stream(models.Model):
    stream_id = models.CharField(max_length=50, primary_key=True)
    stream_name = models.CharField(max_length=150)
    registered = models.DateTimeField(auto_now_add=True)
    modifield_at = models.DateTimeField(auto_now=True)

    streams = models.Manager()

    class Meta:
        db_table = "streams"

class Darasa(models.Model):
    class_id = models.CharField(max_length=50, primary_key=True)
    class_name = models.CharField(max_length=150)
    stream = models.ForeignKey(Stream, on_delete=models.CASCADE)
    registered = models.DateTimeField(auto_now_add=True)
    modifield_at = models.DateTimeField(auto_now=True)

    classes = models.Manager()

    class Meta:
        db_table = "classes"

class Class_subject(models.Model):
    class_subject_id = models.CharField(max_length=50, primary_key=True)
    darasa = models.ForeignKey(Darasa, on_delete=models.CASCADE)
    teacher_subject = models.ForeignKey(Teacher_subject, on_delete=models.CASCADE)

    class_subjects = models.Manager()

    class Meta:
        db_table = "class_subjects"

class Student(models.Model):
    student_id = models.CharField(max_length=50, primary_key=True)
    first_name =models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    standard = models.CharField(max_length=50)
    registration_number = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    modifield_at = models.DateTimeField(auto_now=True)

    students = models.Manager()

    class Meta:
        db_table = "students"

class Exam_type(models.Model):
    exam_id = models.CharField(max_length=50, primary_key=True)
    exam_name = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    modifield_at = models.DateTimeField(auto_now=True)

    examtypes = models.Manager()

    class Meta:
        db_table = "examtypes"

class Year(models.Model):
    year_id = models.CharField(max_length=50, primary_key=True)
    year_name = models.IntegerField(150)
    created_at = models.DateTimeField(auto_now_add=True)
    modifield_at = models.DateTimeField(auto_now=True)

    years = models.Manager()

    class Meta:
        db_table = "years"

class Result(models.Model):
    result_id = models.CharField(max_length=50, primary_key=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    examtype = models.ForeignKey(Exam_type, on_delete=models.CASCADE)
    score = models.IntegerField(50)
    grade = models.CharField(max_length=50)
    year = models.ForeignKey(Year, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modifield_at = models.DateTimeField(auto_now=True)

    results = models.Manager()

    class Meta:
        db_table = "results"




















