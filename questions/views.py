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
        'answer-list':'/answers/',
        'answer-detail':'/answers/<int:pk>/',
        'tag-list':'/tags/',
        'tag-detail':'/tags/<int:pk>/',
    }

class QuestionList(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [User]

    def list(self, request):
        queryset = self.get_queryset()
        serializer = Question.Serializer(queryset, many=True)
        return Response(serializer.data)


class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()

    def get_question(self, pk):
        return Question.objects.get(pk=pk)

    def put(self, request, pk, format=None):
        question = self.get_object(pk)
        serializer = QuestionSerializer(question, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    def delete(self, request, pk, format=None):
        question = self.get_object(pk)
        question.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    
class AnswerList(generics.ListCreateAPIView):
    queryset = Answer.objects.all()
    serializer_class =  AnswerSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = AnswerSerializer(queryset, many=True)
        return Response(serializer.data)

class AnswerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Answer.objects.all()

    def get_answer(self, pk):
        return Answer.objects.get(pk=pk)

    def put(self, request, pk, format=None):
        book = self.get_object(pk)
        serializer = AnswerSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
            



class TagList(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = TagSerializer(queryset, many=True)
        return Response(serializer.data)



class TagDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

    def put(self, request, pk, format=None):
        tag = self.get_object(pk)
        serializer = TagSerializer(tag, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)