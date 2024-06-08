from myClass.models.classPeriod import myClass
from myClass.serializers.classPeriod import myClassSerializers
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

@api_view(['DELETE'])

def myClass_DELETE(request,pk):
    if request.method=='DELETE':
        print("Hello")
        try:
            if pk==None:
                return Response("Please enter user id",status=status.HTTP_404_NOT_FOUND)
            else:
                user=myClass.objects.get(pk=pk)
        except myClass.DoesNotExist:
            return Response("Data not found",status=status.HTTP_404_NOT_FOUND)
        user.delete()
        return Response("Date deleted Successfully",status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
