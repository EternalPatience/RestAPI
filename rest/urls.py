from django.conf.urls import url, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest.views import (SurveyViewSet,
                        QuestionViewSet,
                        SurveyList,
                        QuestionList,
                        UserList,
                        UserDetail)


schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    url(r'^surveys/$', SurveyList.as_view()),
    url(r'^surveys/(?P<pk>[0-9]+)/$', SurveyViewSet.as_view()),
    url(r'^surveys/(?P<pk>[0-9]+)/questions/$', QuestionList.as_view()),
    url(r'^surveys/(?P<pk>[0-9]+)/questions/(?P<id>[0-9]+)', QuestionViewSet.as_view()),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url('users/', UserList.as_view()),
    url('users/<int:pk>/', UserDetail.as_view()),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]


