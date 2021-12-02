from rest_framework import serializers
from .models import Survey, Question
from django.contrib.auth.models import User


class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = ('name', 'start_date', 'end_date', 'description', 'participants')


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('survey', 'type', 'text')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'surveys')


