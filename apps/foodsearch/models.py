from django.db import models
import re, bcrypt

class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    pword = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Recipe(models.Model):
    user = models.ForeignKey(User, related_name="recips")
    recipename = models.CharField(max_length=255)
    picture = models.TextField()
    shortdesc = models.TextField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __repr__(self):
       return f"recipename={self.recipename}"

class Ingre(models.Model):
    ingre_name = models.CharField(max_length=255)
    user = models.ForeignKey(User, related_name="ingre_user")
    recipes = models.ManyToManyField(Recipe, related_name="ingres")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)