from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = ("Categories")
        ordering = ["id",]

    def __str__(self):
        return self.name


class Quiz(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='quiz')
    title = models.CharField(max_length=255, verbose_name=_("Quiz Title"))
    created_date = models.DateTimeField(auto_now_add=True, verbose_name=_("Created Date"))

    class Meta:
        verbose_name = _("Quiz")
        verbose_name_plural = _("Quizzes")
        ordering = ["id",]

    def __str__(self):
        return self.title


class Update(models.Model):
    updated_date = models.DateTimeField(auto_now=True, verbose_name=_("Last Updated"))

    class Meta:
        abstract = True


class Question(Update):
    SCALE = (
        (0, _("Fundamental")),
        (1, _("Beginner")),
        (2, _("Intermediate")),
        (3, _("Advanced")),
        (4, _("Expert")),
    )

    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='question')
    title = models.CharField(max_length=511)
    created_date = models.DateTimeField(auto_now_add=True, verbose_name=_("Created Date"))
    scale = models.IntegerField(default=0, choices=SCALE, verbose_name=_("Scale"))
    is_active = models.BooleanField(default=False, verbose_name=_("Active Status"))

    class Meta:
        verbose_name = _("Question")
        verbose_name_plural = ("Questions")
        ordering = ["id",]

    def __str__(self):
        return self.title


class Answer(Update):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answer')
    answer_text = models.CharField(max_length=255, verbose_name=_("Answer Text"))
    is_true = models.BooleanField(default=False)

    class Meta:
        verbose_name = _("Answer")
        verbose_name_plural = ("Answers")
        ordering = ["id",]

    def __str__(self):
        return self.answer_text
