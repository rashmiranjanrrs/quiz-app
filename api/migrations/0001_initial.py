# Generated by Django 3.1.3 on 2020-11-16 12:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('choice_one', models.CharField(max_length=54)),
                ('choice_two', models.CharField(max_length=54)),
                ('choice_three', models.CharField(max_length=54)),
                ('choice_four', models.CharField(max_length=54)),
                ('answer', models.CharField(max_length=54)),
            ],
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
                ('number_of_questions', models.IntegerField(default=10, max_length=10)),
                ('fetch_question_online', models.BooleanField(default=True)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.CharField(max_length=32)),
                ('time', models.TimeField()),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.quiz')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ResultAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_by_user', models.CharField(max_length=54)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.question')),
                ('result', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.result')),
            ],
        ),
        migrations.CreateModel(
            name='QuizQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.question')),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.quiz')),
            ],
        ),
    ]
