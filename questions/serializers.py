from rest_framework import serializers
from .models import User, Question, Answer, Tag
class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['question', 'user', 'created_at', 'favorited_by', 'tag']
        read_only_fields = ['user', 'created_at']

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['answer', 'user', 'created_at', 'accepted', 'favorited']
        read_only_fields = ['user', 'created_at', 'accepted']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['tag']
        read_only_fields = ['tag']