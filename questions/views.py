from django.shortcuts import render
from rest_framework import generics
from .models import Questions, Answer, Tag
# from .serializers import 

# Create your views here.
class QuestionList(generics.ListCreateAPIView):
    queryset = Questions.objects.all()


class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Questions.objects.all()



class AnswerList(generics.ListCreateAPIView):
    Questions = Answer.objects.all()



class AnswerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Answer.objects.all()
    