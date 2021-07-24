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

    def create(self, validate_data):
        return Question.objects.create(validated_data)

    def update(self, instance, validated_data):
        instance.question = validated_data.get('question', instance.question)
        instance.user = validated_data.get('user', instance.user)
        instance.created_at = validated_data.get('created_at', instance.created_at)
        instance.favorited_by = validated_data.get('favorited_by', instance.favorited_by)
        instance.tag = validated_data.get('tag', instance.tag)
        instance.save()
        return instance

class AnswerSerializer(serializers.ModelSerializer):
    model = Answer
    fields = ['answer', 'user', 'created_at', 'accepted', 'favorited']
    read_only_fields = ['user', 'created_at', 'accepted']

    def create(self, validated_data):
        return Answer.objects.create(validated_data)

class TagSerializer(serializers.ModelSerializer):
    model = Tag
    fields = ['tag']
    read_only_fields = ['tag']