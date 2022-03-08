import uuid

from Users.models import Teacher
from Users.models import Subject
from Users.models import Teacher_subject
from Users.models import Stream
from Users.models import Darasa
import json
from django.contrib.auth.hashers import make_password, check_password

import uuid

#accademic login
def admin_login(data):
    if data['phone_number'] == "0787806932":
        if data['password'] == "0228":
            return json.dumps({'code': 200, 
                               "msg": "wellcome accademic of GPS"})
        else:
            return json.dumps({'code': 300,
                               "msg": "Wrong Password"})

    else:
        return json.dumps({'code': 300,
                           "msg": "Wrong Phone Number"})

def teacher_registration(data):
    for key in data.keys():
        if not data[key]:
            return json.dumps({'code': 200,
                               "msg": key + " " + "is empty"})
    if not Teacher.teachers.filter(email=data['email']).exists():
        new_teacher = Teacher()
        new_teacher.teacher_id = uuid.uuid4()
        new_teacher.teacher_name = data["teacher_name"]
        new_teacher.phone_number = data['phone_number']
        new_teacher.email = data["email"]
        new_teacher.password = make_password(data["password"])
        new_teacher.save()
        return json.dumps({'code': 200,
                           "msg": "Teacher registration successfully"})
    else:
        return json.dumps({"code": 200,
                           "msg": "email is exist"})

def teacher_login(request):
    for key in request.keys():
        if not request[key]:
            return json.dumps({'code': 200,
                               "msg": key + " " + "is empty"})
    if Teacher.teachers.filter(email=request['email']).exists():
        teacher = Teacher.teachers.get(email=request['email'])
        if check_password(request.get('password'), teacher.password):
            response = {
                "code": 200,
                "user_detail": {
                    "teacher_id": teacher.teacher_id,
                    "teacher_name": teacher.teacher_name,
                    "email": teacher.email,
                    "phone_number": teacher.phone_number
                }
            }
            return json.dumps(response)
        else:
            return json.dumps({'code': 200,
                               "msg": "Incorrect password"})
    else:
        return json.dumps({'code': 200,
                          "msg": "Incorrect email"})


def password_recovery(data):
    for key in data.keys():
        if not data[key]:
            return json.dumps({'code': 200,
                               "msg": key + " " + "is empty"})
    if Teacher.teachers.all().filter(email=data['email']).exists():
        student = Teacher.teachers.get(email=data['email'])
        student.password = make_password(data['password'])
        student.save()
        return json.dumps({'code': 200, "msg": "Password Successfully Recovered"})
    else:
        return json.dumps({"code": 300, "msg": "Email Doesnt not Exist"})

def subject_registration(data):
    for key in data.keys():
        if not data[key]:
            return json.dumps({'code': 200,
                               "msg": key + " " + "is empty"})
    if not Subject.subjects.filter(subject_name=data["subject_name"]).exists():
        new_subject = Subject()
        new_subject.subject_id = uuid.uuid4()
        new_subject.subject_name = data["subject_name"]
        new_subject.save()
        return json.dumps({'code': 200,
                           "msg": "subject registered"})
    else:
        return json.dumps({'code': 200,
                           "msg": "subject is exist"})



def subject_teacher(data):
    for key in data.keys():
        if not data[key]:
            return json.dumps({'code': 200,
                               "msg": key + " " + "is empty"})

        new = Teacher_subject()
        new.subject_teacher_id = uuid.uuid4()
        new.teacher_id = data["teacher_id"]
        new.subject_id = data["subject_id"]
        new.save()
        return json.dumps({'code': 200,
                           "msg": "teacher subject added"})
def stream(data):
    for key in data.keys():
        if not data[key]:
            return json.dumps({'code': 200,
                               "msg": key + " " + "is empty"})
    if not Stream.streams.filter(stream_name=data["stream_name"]).exists():
        new_stream =Stream()
        new_stream.stream_id = uuid.uuid4()
        new_stream.stream_name = data["stream_name"]
        new_stream.save()
        return json.dumps({'code': 200,
                           "msg": "stream added"})
    else:
        return json.dumps({'code': 200,
                           "msg": "stream is exist"})

def darasa(data):
    for key in data.keys():
        if not data[key]:
            return json.dumps({'code': 200,
                               "msg": key + " " + "is empty"})
    if not Darasa.classes.filter(class_name=data["class_name"]).exists():
        new_class = Darasa()
        new_class.class_name = data["class_name"]
        new_class.stream_id = data["stream_id"]
        new_class.save()
        return json.dumps({'code': 200,
                            "msg": "class added"})
    else:
        return json.dumps({'code': 200,
                           "msg": "class is exists"})






