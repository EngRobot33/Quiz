from django.urls import path
from .views import Quiz, RandomQuestion, QuizQuestion

app_name = 'quiz'

urlpatterns = [
    path('', Quiz.as_view(), name='quiz'),
    path('random/<str:topic>/', RandomQuestion.as_view(), name='random'),
    path('<str:topic>/', QuizQuestion.as_view(), name='question'),
]