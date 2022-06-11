from dataclasses import field
from rest_framework import serializers
from .models import Quiz

class QuizSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()

    class Meta:
        model = Quiz
        fields = ['title', 'category']
