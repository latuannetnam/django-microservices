from dynamic_rest.fields.fields import DynamicRelationField
from dynamic_rest.serializers import DynamicModelSerializer
from rest_framework.fields import IntegerField, SerializerMethodField
from .models import Question, Choice


class QuestionSerializer(DynamicModelSerializer):
    choices = DynamicRelationField('ChoiceSerializer', many=True, required=False)

    class Meta:
        model = Question
        name = 'question'
        fields = ('id', 'question_text', 'pub_date', 'choices')
        deferred_fields = ('choices', )


class ChoiceSerializer(DynamicModelSerializer):
    question = DynamicRelationField(
        QuestionSerializer, many=False, required=False)

    class Meta:
        model = Choice
        name = 'choice'
        fields = ('id', 'choice_text', 'votes', 'question')
        defered_fields = ('question')
