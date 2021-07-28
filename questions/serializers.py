from rest_framework import serializers
from .models import User, Question, Answer, Tag

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['question', 'user', 'created_at', 'favorited_by', 'tag']
        read_only_fields = ['user', 'created_at']

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['answer', 'user', 'created_at', 'question']
        read_only_fields = ['user', 'created_at']

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['tag']
        read_only_fields = ['tag']