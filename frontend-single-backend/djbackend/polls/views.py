from django.shortcuts import render
from dynamic_rest.viewsets import DynamicModelViewSet
from rest_framework.permissions import DjangoModelPermissions
from .models import Question, Choice
from .serializers import QuestionSerializer, ChoiceSerializer
# Create your views here.


class ChoiceViewSet(DynamicModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer


class QuestionViewSet(DynamicModelViewSet):
    queryset = Question.objects.all().order_by('-pub_date')
    serializer_class = QuestionSerializer    
