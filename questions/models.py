import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE




class User(AbstractUser):
    def __str__(self):
        return self.username


<<<<<<< HEAD
class Questions(models.Model):
    question = models.TextField()
    user = models.ForeignKey(User, on_delete=CASCADE, related_name='question_user')
    created_at = models.DateField(auto_now_add=True)
    favorited_by = models.ManyToManyField(User)

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
=======
class Question(models.Model):
    question = models.TextField()
    user = models.ForeignKey(User, on_delete=CASCADE, related_name='question_user')
    created_at = models.DateField(auto_now_add=True)
    favorited_by = models.ManyToManyField(User, related_name='favorited', null=True, blank=True)
    tag = models.ManyToManyField('Tag', related_name='questions', null=True, blank=True)
>>>>>>> 2697d904731943e5ef85a9c8e1042ea14f423a9f


class Answer(models.Model):
    answer = models.TextField()
    user = models.ForeignKey(User, on_delete=CASCADE, related_name='answer_user')
    created_at = models.DateField(auto_now_add=True)
    accepted = models.BooleanField()
    favorited = models.BooleanField()
<<<<<<< HEAD
    question = models.ForeignKey(Questions, on_delete=CASCADE)
=======
    question = models.ForeignKey(Question, on_delete=CASCADE)
>>>>>>> 2697d904731943e5ef85a9c8e1042ea14f423a9f
    

class Tag(models.Model):
    tag = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.tag
