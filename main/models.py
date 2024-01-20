from django.db import models
import re
from django.db import models
from django.core.validators import RegexValidator

class Banner(models.Model):
    img = models.ImageField(upload_to='banner-photos/')
    about_me = models.TextField()


class About(models.Model):
    title = models.CharField(max_length=55)
    text = models.TextField()


class Info(models.Model):
    full_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    website = models.CharField(max_length=55)
    email = models.CharField(max_length=255,  validators=[
        RegexValidator(
            regex='^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',
            message='Invalide email',
            code='Invalid email'
        )
    ])


class People_say(models.Model):
    img = models.ImageField(upload_to='people-photos/')
    name = models.CharField(max_length=55)
    description = models.CharField(max_length=55)

class Fac(models.Model):
    question = models.CharField(max_length=255)
    answer = models.CharField(max_length=255)

class Contact(models.Model):
    full_name = models.CharField(max_length=55)
    email = models.CharField(max_length=255,  validators=[
        RegexValidator(
            regex='^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',
            message='Invalide email',
            code='Invalid email'
        )
    ])
    message = models.TextField()
    phone_number = models.CharField(max_length=13, null=True, blank=True, validators=[
        RegexValidator(
            regex='^[\+]9{2}8{1}[0-9]{9}$',
            message='Invalide phone number',
            code='Invalid number'
        )
    ])
    facebook = models.CharField(max_length=55, null=True, blank=True,)
    twitter = models.CharField(max_length=55, null=True, blank=True,)
    instagram = models.CharField(max_length=55, null=True, blank=True, )
    yutube = models.CharField(max_length=55, null=True, blank=True, )




