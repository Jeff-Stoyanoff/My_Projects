from ast import In
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import IntegerField, TextField, DateTimeField
import re, bcrypt

class OwnerManager(models.Manager):
    def Registration_validator(self, postData):
        errors = {}
        if len(postData['firstname']) < 1:
            errors['firstnameshort'] = "No First Name given"
        if len(postData['lastname']) < 1:
            errors['lastnameshort'] = "No Last Name given"
        if len(Player.objects.filter(email=postData['email'])) > 0:
            errors['existingEmail'] = "User already registered with that email"
        Email_Regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not Email_Regex.match(postData['email']):
            errors['invalidEmail'] = "Invalid Email Address"
        if len(postData['password']) < 8:
            errors['passwordshort'] = "Password must be at least 8 characters"
        return errors
        
    def Login_validator(self, postData):
        errors = {}
        checkUser = Player.objects.filter(email = postData['logemail'])
        if len(checkUser) < 1:
            errors['noEmail'] = "Invalid Email or Password"
        elif not bcrypt.checkpw(postData['logpassword'].encode(), checkUser[0].password.encode()):
            errors['passwordnomatch'] = "Incorrect Email and/or Password"
        return errors

class Player(models.Model):
    firstname = models.CharField(max_length=75)
    lastname = models.CharField(max_length=155)
    email = models.CharField(max_length=80)
    password = models.CharField(max_length=80)
    points = models.IntegerField(default = 0)
    answer = models.CharField(max_length=155)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)
    objects = OwnerManager()

class Question(models.Model):
    text = models.CharField(max_length=300)
    answer = models.CharField(max_length=300)
    category = models.CharField(max_length=80)
    level = models.IntegerField()
    asked = models.BooleanField(default=False)
    media = models.BooleanField(default=False)
    image = models.ForeignKey('Image', on_delete=models.CASCADE, null=True, blank=True)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    def get_answers_list(self):
        return[answer.strip() for answer in self.answers.split(',')]

    def __str__(self):
        return self.text
    
class Answer(models.Model):
    text = models.CharField(max_length=300)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

class Image(models.Model):
    name = models.CharField(max_length=100)
    file = models.ImageField(upload_to='images/')  # Specify the upload path


    def __str__(self):
        return self.name

