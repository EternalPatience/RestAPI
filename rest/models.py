from django.db import models
from django.conf import settings


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
    participants = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='surveys',
        verbose_name='Участник'
    )

    class Meta:
        ordering = ('start_date',)
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'


class Question(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, verbose_name='Опрос')
    type = models.CharField(choices=types, verbose_name='Тип', max_length=1)
    text = models.TextField(verbose_name='Текст вопроса')

    class Meta:
        ordering = ('survey',)
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    def __str__(self):
        return self.text

