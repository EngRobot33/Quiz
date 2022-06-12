from dataclasses import field
from rest_framework import serializers
from .models import Quiz, Question

class QuizSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()

    class Meta:
        model = Quiz
        fields = ['title', 'category']


class RandomQuestionSerializer(serializers.ModelSerializer):
    answer = serializers.StringRelatedField(many=True)

    class Meta:
        model = Question
        fields = ['title', 'answer',]
