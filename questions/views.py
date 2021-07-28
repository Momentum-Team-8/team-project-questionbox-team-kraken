from .models import Question, Answer, Tag, User
from .serializers import QuestionSerializer, AnswerSerializer, UserSerializer, TagSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

from questions import serializers
# from .serializers import 

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
@permission_classes(IsAuthenticatedOrReadOnly)
def questionCreate(request):#save logged user in request
    serializer = QuestionSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save(user=request.user)
    
    return Response(serializer.data)

@api_view(['PUT'])
def questionEdit(request, pk):
    question = Question.objects.get(id=pk)
    serializer = QuestionSerializer(instance=question, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
@permission_classes(IsAuthenticated)
def questionDelete(request, pk):
    question = Question.objects.get(id=pk)
    user = User.objects.get(id=pk)
    if question == user:
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
@permission_classes(IsAuthenticatedOrReadOnly)
def answerCreate(request):
    serializer = AnswerSerializer(data=request.data)
    question=Question.objects.get(id=request.data["question"])

    if serializer.is_valid():
        serializer.save(user=request.user, question=question)
    
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