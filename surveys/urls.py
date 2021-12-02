from django.urls import path
from .views import index, survey, ParticipateInSurvey, personal_surveys


app_name = 'surveys'

urlpatterns = [
    path('', index, name='index'),
    path('<int:pk>/', survey, name='survey'),
    path('<int:pk>/participate', ParticipateInSurvey.as_view(), name='participate'),
    path('personal/', personal_surveys, name='personal'),

]
