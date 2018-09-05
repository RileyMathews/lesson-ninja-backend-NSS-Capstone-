from django.db import models
from .user import User
from .student import Student

class Teacher(models.Model):
    bio = models.CharField(max_length=500, blank=True)
    street = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    region = models.CharField(max_length=255, blank=True)
    country = models.CharField(max_length=255, blank=True)
    zip_code = models.IntegerField(blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student, through='TeacherStudent')

    def __str__(self):
        return f'teacher {self.user}'