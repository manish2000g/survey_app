from rest_framework import serializers
from .models import Survey, SurveyLink

class SurveyLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = SurveyLink
        fields = '__all__'

class SurveySerializer(serializers.ModelSerializer):
    survey_links = SurveyLinkSerializer(many=True, read_only=True)

    class Meta:
        model = Survey
        fields = '__all__'
