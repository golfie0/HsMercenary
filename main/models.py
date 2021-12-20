from django.db import models
import uuid

# Create your models here.

class Card(models.Model):
    title = models.CharField('Название карты', max_length=50)


class User(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_name = models.CharField('UserName', unique=True, max_length=32)
    email = models.EmailField('Email', max_length=254)

class Deck(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    cards = models.ManyToManyField(Card)
    title = models.CharField('Название карты', max_length=50)
    

class Post(models.Model):
    pass

class Comment(models.Model):
    pass