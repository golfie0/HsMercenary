from typing import Text
from django.db import models
import uuid
# Create your models here.

class Card(models.Model):
    title = models.CharField('Название карты', max_length=50)

    
    def __str__(self):
        return self.title


class User(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    user_name = models.CharField('UserName', unique=True, max_length=32)
    email = models.EmailField('Email', max_length=254, unique=True)
    register_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user_name

class Deck(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    cards = models.ForeignKey(Card, on_delete=models.CASCADE)
    title = models.CharField('Название колоды', max_length=50)

    def __str__(self):
        return self.title

class Post(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    title = models.CharField(max_length=50)
    text = models.TextField(max_length=600)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # vote_total
    # vote_ratio
    # demo_link
    # source_link

    def __str__(self):
        return self.title

class Comment(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    text = models.TextField(max_length=600)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.text

# class Rating(models.Model):
#     # post = models.ForeignKey(Post, on_delete=models.CASCADE)
#     # RATING_TYPE=(
#     #     ('up', 'up'),
#     #     ('down', 'down'),
#     # )
#     # value = models.CharField(max_length=10, choices=RATING_TYPE)
#     pass