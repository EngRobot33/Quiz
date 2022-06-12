from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Quiz, Question
from .serializers import QuizSerializer, RandomQuestionSerializer

class Quiz(ListAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer


class RandomQuestion(APIView):
    def get(self, request, format=None, **kwargs):
        question = Question.objects.filter(quiz__title=kwargs['topic']).order_by("?")[:1]
        serializer = RandomQuestionSerializer(question, many=True)
        return Response(serializer.data)
