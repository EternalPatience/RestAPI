from .models import Survey, Question
from django.contrib.auth.models import User
from rest_framework import permissions
from .serializers import SurveySerializer, QuestionSerializer, UserSerializer
from rest_framework import mixins, generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse


"""@api_view(['GET'])
def api_root(request):
    return Response({
        'users': reverse(UserList, request=request),
        'surveys': reverse(SurveyList, request=request),
        'questions': reverse(QuestionList, request=request),
    })"""


class SurveyList(APIView):
    """List all surveys"""
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]
    queryset = Survey.objects.all().order_by('start_date')

    def get(self, request, format=None):
        surveys = Survey.objects.all()
        serializer = SurveySerializer(surveys, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SurveySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user.id)


class SurveyViewSet(mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    """View survey and require CRUD"""
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]
    queryset = Survey.objects.all().order_by('start_date')
    serializer_class = SurveySerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class QuestionList(APIView):
    """List all surveys"""
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]
    queryset = Question.objects.all()

    def get(self, request, pk, format=None):
        questions = Question.objects.filter(survey__question=pk)
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user.id)


class QuestionViewSet(mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      generics.GenericAPIView):
    """View all questions in a survey"""
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

