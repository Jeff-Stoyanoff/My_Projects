from ast import In
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import IntegerField, TextField, DateTimeField
import re, bcrypt

class Player(models.Model):
    current = models.BooleanField(default=True)
    name = models.CharField(max_length=255)
    rank = models.IntegerField()
    cost = models.IntegerField()
    points = models.IntegerField(default=0)
    about = models.CharField(max_length=200)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

class Team(models.Model):
    current = models.BooleanField(default=True)
    name = models.CharField(max_length=155)
    draftedPlayer = models.ManyToManyField(Player, related_name="teamDrafted")
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

class Tournament(models.Model):
    current = models.BooleanField(default=True)
    name = models.TextField(max_length=155)
    budget = models.IntegerField()
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)




