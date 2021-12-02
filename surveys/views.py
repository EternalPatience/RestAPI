from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from rest.models import Survey, Question
from django.contrib.auth.models import User
from django import forms


def index(request):
    """Main page"""
    surveys = Survey.objects.all().order_by('end_date')
    return render(request, 'surveys/index.html', {'surveys': surveys})


def survey(request, pk):
    survey = Survey.objects.get(pk=pk)
    questions = Question.objects.filter(survey=survey)
    context = {'survey': survey, 'questions': questions}
    return render(request, 'surveys/survey.html', context)


class SurveyForm(forms.ModelForm):
    class Meta:
        model = Survey
        fields = ('__all__')


class ParticipateInSurvey(CreateView):
    model = Survey
    form_class = SurveyForm
    success_url = reverse_lazy('survey:index')
    template_name = 'surveys/participant.html'


def personal_surveys(request):
    surveys = Survey.objects.filter(participants=request.user)
    return render(request, 'surveys/personal.html', {'surveys': surveys})