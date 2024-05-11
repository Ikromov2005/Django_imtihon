import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser

from .managers import UserManager


class User(AbstractUser):
    first_name = models.CharField(max_length=100, verbose_name="Ism")
    last_name = models.CharField(max_length=100, verbose_name="Familiya")
    username = models.CharField(max_length=100, blank=True, verbose_name="Username")
    email = models.CharField(max_length=100, unique=True, verbose_name="E-mail manzil")
    profile_image = models.ImageField(
    upload_to='images/', default='images/profile_image.png', null=True, blank=True, verbose_name="Profil rasmi")
    is_staff = models.BooleanField(default=False, verbose_name="Xodimlik statusi")
    is_superuser = models.BooleanField(default=False, verbose_name="Superuser statusi")
    is_active = models.BooleanField(default=True, verbose_name="Akkauntning faollik statusi")
    objects = UserManager()

    REQUIRED_FIELDS = ['first_name', 'last_name', 'username']
    USERNAME_FIELD = 'email'

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Hobby(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Student(models.Model):
    teacher = models.ForeignKey(to=User, on_delete=models.PROTECT)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    hobbies = models.ManyToManyField(to=Hobby)
    id = models.UUIDField(default=uuid.uuid4, editable=False,
                          primary_key=True, unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Book(models.Model):
    student = models.OneToOneField(to=Student, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.student.first_name} {self.student.last_name} - {self.title}"
    



class Note(models.Model):
    id = models.UUIDField(unique=True, primary_key=True, editable=False, default=uuid.uuid4)
    title = models.CharField(max_length=200)
    body = models.TextField(null=True, blank=True)
    is_done = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title