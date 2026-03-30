from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=150)
    gender = models.CharField(max_length=10, choices= [('Male', 'Male'),('Female', 'Female')])
    city = models.CharField(max_length=15)
    state = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    college = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

