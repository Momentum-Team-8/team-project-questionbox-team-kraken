import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE




class User(AbstractUser):
    def __str__(self):
        return self.username


class Question(models.Model):
    title = models.TextField(max_length=250, null=True, blank=True, default="Subject")
    question = models.TextField()
    user = models.ForeignKey(User, on_delete=CASCADE, related_name='question_user')
    created_at = models.DateField(auto_now_add=True)
    favorited_by = models.ManyToManyField(User, related_name='favorited', null=True, blank=True)
    tag = models.ManyToManyField('Tag', related_name='questions', null=True, blank=True)


class Answer(models.Model):
    answer = models.TextField()
    user = models.ForeignKey(User, on_delete=CASCADE, related_name='answer_user')
    created_at = models.DateField(auto_now_add=True)
    accepted = models.BooleanField(null=True, blank=True)
    favorited = models.BooleanField(null=True, blank=True)
    question = models.ForeignKey(Question, on_delete=CASCADE)
    

class Tag(models.Model):
    tag = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.tag
