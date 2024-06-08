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
            python_data=request.data 
            python_data1={
                'faculty_name':python_data.get('faculty_name'),
                'date':python_data.get('date'),
                'start':python_data.get('start'),
                'end':python_data.get('end'),
                'course':python_data.get('course'),
                'description':python_data.get('description')
            }
            user=myClass.objects.all()
            serializer1=myClassSerializers(user,many=True)
            for d in serializer1.data:
                d1={
                'faculty_name':d.get('faculty_name'),
                'date':d.get('date'),
                'start':d.get('start'),
                'end':d.get('end'),
                'course':d.get('course'),
                'description':d.get('description')
            }
                if d1['course']==python_data1['course'] and d1['date']==python_data1['date'] and d1['faculty_name']==python_data1['faculty_name']:
                        return Response("Record already saved !")
            serializer = myClassSerializers(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response("Record Save Successfully", status=status.HTTP_201_CREATED)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
