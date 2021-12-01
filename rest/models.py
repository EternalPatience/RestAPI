from django.db import models
from django.contrib.auth.models import User


types = [
    ('1', 'ответ текстом',),
    ('2', 'ответ с выбором одного варианта',),
    ('3', 'ответ с выбором нескольких вариантов')
]


class Survey(models.Model):
    name = models.CharField(verbose_name='Название', max_length=200)
    start_date = models.DateField(verbose_name='Дата начала', auto_now_add=True, editable=False)
    end_date = models.DateField(verbose_name='Дата окончания')
    description = models.TextField(verbose_name='Описание')
    participant = models.ForeignKey(User, related_name='surveys', on_delete=models.CASCADE, verbose_name='Участник')

    class Meta:
        ordering = ('start_date',)
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'


class Question(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, verbose_name='Опрос')
    type = models.CharField(choices=types, verbose_name='Тип', max_length=1)
    text = models.TextField(verbose_name='Текст')

    class Meta:
        ordering = ('survey',)
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'
