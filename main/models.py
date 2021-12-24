from typing import Text
from django.db import models
import uuid
from django.utils.timezone import now
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
    # pass_hash = models.CharField()
    def __str__(self):
        return self.user_name

class Deck(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField('Название колоды', max_length=50)
    cards = models.ManyToManyField(Card, blank=True) # убрать blank true

    def __str__(self):
        return self.title

class Post(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    title = models.CharField(max_length=50)
    text = models.TextField(max_length=600)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    attached_deck = models.ForeignKey(Deck, on_delete=models.CASCADE, null=True, blank=True) # убрать нул бланк
    # vote_total
    # vote_ratio
    # demo_link
    # source_link

    def __str__(self):
        return self.title

class Comment(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    text = models.TextField(max_length=600)
    posted_time = models.DateTimeField(default=now, blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    attached_to = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True) # убрать null=True, blank=True

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