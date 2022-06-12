from atexit import register
from django.contrib import admin
from .models import Category, Quiz, Question, Answer


class QuizAdmin(admin.ModelAdmin):
    list_display = ['title', 'category']

admin.site.register(Quiz, QuizAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name',]

admin.site.register(Category, CategoryAdmin)


class AnswerInlineModel(admin.TabularInline):
    model = Answer
    fields = ['answer_text', 'is_true',]


class QuestionAdmin(admin.ModelAdmin):
    list_display = ['title',]
    inlines = [AnswerInlineModel,]

admin.site.register(Question, QuestionAdmin)


class AnswerAdmin(admin.ModelAdmin):
    list_display = ['answer_text', 'is_true',]

admin.site.register(Answer, AnswerAdmin)
