from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from survey.serializers import SurveySerializer
from .models import Survey

@api_view(['GET'])
def get_surveys(request):
    surveys = Survey.objects.all()
    serializer = SurveySerializer(surveys, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
