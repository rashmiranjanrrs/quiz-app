from rest_framework import serializers
from .models import Question, Quiz, Result
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only':True, 'required':True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('category','type', 'difficulty', 'question', 'correct_answer','incorrect_answers')

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ('id', 'title', 'number_of_questions','fetch_question_online', 'status')

class QuizMainSerializer(serializers.ModelSerializer):
    results = QuestionSerializer(many=True)
    class Meta:
        model = Quiz
        fields = ('results', )

class ResultSerializer(serializers.ModelSerializer):
    quiz = QuizSerializer(many=False)
    class Meta:
        model = Result
        fields = ('id', 'quiz','correct_answers','incorrect_answers', 'time')