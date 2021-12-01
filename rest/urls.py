from django.conf.urls import url, include
from rest.views import (SurveyViewSet,
                        QuestionViewSet,
                        SurveyList,
                        QuestionList,
                        UserList,
                        UserDetail)


urlpatterns = [
    url(r'^surveys/$', SurveyList.as_view()),
    url(r'^surveys/(?P<pk>[0-9]+)/$', SurveyViewSet.as_view()),
    url(r'^surveys/(?P<pk>[0-9]+)/questions/$', QuestionList.as_view()),
    url(r'^surveys/(?P<pk>[0-9]+)/questions/(?P<id>[0-9]+)', QuestionViewSet.as_view()),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url('users/', UserList.as_view()),
    url('users/<int:pk>/', UserDetail.as_view()),
]


