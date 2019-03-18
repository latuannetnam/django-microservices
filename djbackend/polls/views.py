from django.shortcuts import render
from dynamic_rest.viewsets import DynamicModelViewSet
from rest_framework.permissions import DjangoModelPermissions
from rest_framework import permissions
from .models import Question, Choice
from .serializers import QuestionSerializer, ChoiceSerializer
# Create your views here.


class ChoiceViewSet(DynamicModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer


class QuestionViewSet(DynamicModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Question.objects.all().order_by('-pub_date')
    serializer_class = QuestionSerializer
