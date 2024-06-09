from feedback.models.feedback import Model_Feedback
from feedback.serializers.feedback import Serializers_Feedback
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class View_Feedback(APIView):
    def get(self, request, format=None):
        snippets = Model_Feedback.objects.all()
        serializer = Serializers_Feedback(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = Serializers_Feedback(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)