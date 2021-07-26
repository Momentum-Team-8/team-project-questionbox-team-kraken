from rest_framework import serializers
from .models import User, Question, Answer, Tag


    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email', 'first_name', 'last_name']
        write_only_fields = ['password',]
        read_only_fields = ['id',]

        def create(self, validated_data):
            user = User.objects.create(
                username=validated_data['username'],
                email=validated_data['email'],
                first_name=validated_data['first_name'],
                last_name=validated_data['last_name']
            )
            user.set_password(validated_data['password'])
            user.save()
            return user

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