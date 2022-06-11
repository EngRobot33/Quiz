from rest_framework.generics import ListAPIView
from .models import Quiz
from .serializers import QuizSerializer

class Quiz(ListAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
