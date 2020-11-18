from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import UserSerializer, QuizSerializer, ResultSerializer,QuizMainSerializer
from .models import Question, Quiz, Result


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def update(self, request, pk=None):
        message = {'message': 'Not allowed.'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)
    def destroy(self, request, pk=None):
        message = {'message': 'Not allowed.'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)

class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    def list(self, request):
        try:
            quizzes = Quiz.objects.filter(status=True)
            serializer_result = QuizSerializer(quizzes, many=True)
            return Response(serializer_result.data)
        except:
            message = {'message': 'Currently no quiz available.'}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        message = {'message': 'Not allowed.'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        message = {'message': 'Not allowed.'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        try:
            quiz = Quiz.objects.get(id=pk, status=True)
            serializer_result = QuizMainSerializer(quiz)
            return Response(serializer_result.data, status=status.HTTP_200_OK)
        except:
            message = {'message': 'Currently no quiz available.'}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)

class ResultViewSet(viewsets.ModelViewSet):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )
    def create(self, request):
        user = request.user
        quiz = Quiz.objects.get(request.data['quiz'])
        result = Result.objects.create(user=user, quiz=quiz, correct_answers=request.data['correct_answers'], incorrect_answers=request.data['incorrect_answers'])
        message = {'message': 'Successully submited.'}
        return Response(message, status=status.HTTP_200_OK)

    def list(self, request):
        try:
            user = request.user
            result = Result.objects.get(user=user)
            serializer_result = ResultSerializer(result)
            return Response(serializer_result.data, status=status.HTTP_200_OK)
        except:
            message = {'message': 'You have not appeared any Quiz.'}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        message = {'message': 'Not allowed.'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        message = {'message': 'Not allowed.'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)