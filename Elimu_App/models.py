from django.db import models

# Create your models here.
from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User




class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    instructor = models.CharField(max_length=255)
    image = models.ImageField(upload_to='course_images/', null=True, blank=True)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

class Question(models.Model):
    CATEGORY_CHOICES = [
        ('python', 'Python'),
        ('javascript', 'Javascript'),
        ('java', 'Java'),
        ('ruby', 'Ruby'),
        ('php', 'Php'),
        ('html & css', 'Html & Css'),
        ('kotlin', 'Kotlin'),
        ('flutter', 'Flutter'),
    ]

    category = models.CharField(max_length=50)
    question = models.TextField()
    option1 = models.CharField(max_length=255)
    option2 = models.CharField(max_length=255)
    option3 = models.CharField(max_length=255)
    option4 = models.CharField(max_length=255)
    answer = models.CharField(max_length=255)

    def __str__(self):
        return self.question

class Student(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    mobile = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Tutorial(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    video = models.FileField(upload_to='videos/', null=True, blank=True)

    def __str__(self):
        return self.title

class Instructor(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    mobile = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Topic(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title

class Result(models.Model):
    username = models.CharField(max_length=100)
    topic_name = models.CharField(max_length=100)
    good = models.BooleanField(default=False)
    fail = models.BooleanField(default=False)
    date = models.DateTimeField(default=now)
    marks = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        if self.good:
            status = "Pass"
        elif self.fail:
            status = "Fail"
        else:
            status = "Pending"
        return f"{self.username} - {self.topic_name} - {status} ({self.marks} marks)"



class Profile(models.Model):
    ROLE_CHOICES = [
        ('student', 'Student'),
        ('instructor', 'Instructor'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='student')

    def __str__(self):
        return self.user.username
