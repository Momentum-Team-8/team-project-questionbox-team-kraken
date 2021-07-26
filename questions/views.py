from django.shortcuts import render
from rest_framework import generics
from .models import Question, Answer, Tag, User
from .serializers import QuestionSerializer, AnswerSerializer, UserSerializer, TagSerializer
from rest_framework import generics, status
from rest_framework.permissions import IsAdminUser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
import io
# from .serializers import 

# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'question-list':'/questions/',
        'question-detail':'/questions/<int:pk/',
        'question-create':'/questions/',
        'question-edit':'/questions/',
        'question-delete':'/questions',
        'answer-list':'/answers/',
        'answer-detail':'/answers/<int:pk>/',
        'answer-create':'/answers/',
        'tag-list':'/tags/',
        'tag-detail':'/tags/<int:pk>/',
        'tag-create':'/tags/<int:pk>/'
    }

    return Response("API BASE POINT", safe=False)


@api_view(['GET'])
def questionList(request):
    questions = Question.objects.all()
    serializer = QuestionSerializer(questions, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def questionDetail(request, pk):
    questions = Question.objects.get(id=pk)
    serializer = QuestionSerializer(questions, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def questionCreate(request):
    serializer = QuestionSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)

@api_view(['POST'])
def questionEdit(request, pk):
    question = Question.objects.get(id=pk)
    serializer = QuestionSerializer(instance=question, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def questionDelete(request, pk):
    question = Question.objects.get(id=pk)
    question.delete()

    return Response('Your question has been deleted.')

@api_view(['GET'])
def answerList(request):
    answers = Answer.objects.all()
    serializer = AnswerSerializer(answers, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def answerDetail(request, pk):
    answers = Answer.objects.get(id=pk)
    serializer = AnswerSerializer(answers, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def answerCreate(request):
    serializer = AnswerSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)

@api_view(['GET'])
def tagList(request):
    tags = Tag.objects.all()
    serializer = TagSerializer(tags, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def tagDetail(request, pk):
    tags = Tag.objects.get(id=pk)
    serializer = TagSerializer(tags, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def tagCreate(request):
    serializer = TagSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)