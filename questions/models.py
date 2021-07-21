import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE




class User(AbstractUser):
    def __str__(self):
        return self.username


class Questions(models.Model):
    question = models.TextField()
    user = models.ForeignKey(User, on_delete=CASCADE)
    created_at = models.DateField(auto_now_add=True)
    favorited_by = models.ManyToManyField()

    def get_tag_names(self):
        tag_names = []
        for tag in self.tags.all():
            tag_names.append(tag.tag)

        return " ".join(tag_names)

    def set_tag_names(self, tag_names):
        tag_names = tag_names.split()
        tags = []
        for tag_name in tag_names:
            tag = Tag.objects.filter(tag=tag_name).first()
            if tag is None:
                tag = Tag.objects.create(tag=tag_name)
            tags.append(tag)
        self.tags.set(tags)


class Answer(models.Model):
    answer = models.TextField()
    user = models.ForeignKey(User, on_delete=CASCADE)
    created_at = models.DateField(auto_now_add=True)
    accepted = models.BooleanField()
    favorited = models.BooleanField()
    question = models.ForeignKey(Questions, on_delete=CASCADE)
    

class Tag(models.Model):
    tag = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.tag
