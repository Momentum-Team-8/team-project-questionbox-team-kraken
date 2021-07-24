from django.shortcuts import render
from rest_framework import generics
from .models import Question, Answer, Tag
# from .serializers import 

# Create your views here.
class QuestionList(generics.ListCreateAPIView):
    queryset = Question.objects.all()


class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()



class AnswerList(generics.ListCreateAPIView):
    queryset = Answer.objects.all()



class AnswerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Answer.objects.all()



class TagList(generics.ListCreateAPIView):
    queryset = Tag.objects.all()



class TagDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()