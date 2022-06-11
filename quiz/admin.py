from atexit import register
from django.contrib import admin
from .models import Category, Quiz


class QuizAdmin(admin.ModelAdmin):
    list_display = ['title', 'category']

admin.site.register(Quiz, QuizAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name',]

admin.site.register(Category, CategoryAdmin)
