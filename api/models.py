from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class Question(models.Model):
    question = models.TextField()
    class Enum(models.TextChoices):
        BOOLEAN = 'boolean', _('Boolean')
        MULTIPLE = 'multiple', _('Multiple')

    question_type = models.CharField(
        max_length=12,
        choices=Enum.choices,
        default=Enum.MULTIPLE,
    )
    choice_one = models.CharField(max_length = 54)
    choice_two = models.CharField(max_length = 54)
    choice_three = models.CharField(max_length = 54)
    choice_with_answer = models.CharField(max_length = 54)

    def incorrect_answers(self):
        incorrect_answers = [self.choice_one, self.choice_two, self.choice_three]
        return incorrect_answers

    def correct_answer(self):
        return self.choice_with_answer

    def category(self):
        return ''

    def type(self):
        return self.question_type

    def difficulty(self):
        return ''

class Quiz(models.Model):
    title = models.CharField(max_length=32)
    number_of_questions = models.IntegerField(default=10)
    fetch_question_online = models.BooleanField(default=True)
    status = models.BooleanField(default=True)
    questions = models.ManyToManyField(Question)

    def results(self):
        return self.questions

class Result(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    correct_answers = models.CharField(max_length=32)
    incorrect_answers = models.CharField(max_length=32)
    time = models.TimeField()