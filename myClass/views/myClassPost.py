from myClass.models.classPeriod import myClass
from myClass.serializers.classPeriod import myClassSerializers
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

@api_view(['POST'])

def myClass_POST(request):
    if request.method=='POST':
        try:
            serializer = myClassSerializers(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response("Record Save Successfully", status=status.HTTP_201_CREATED)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
