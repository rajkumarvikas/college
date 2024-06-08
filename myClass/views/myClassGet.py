from myClass.models.classPeriod import myClass
from myClass.serializers.classPeriod import myClassSerializers
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

@api_view(['POST','POST'])


def myClass_Get(request):
    if request.method=='POST':
        try:
            data=request.data
            course=data.get('course')
            date=data.get('date')
            dic={}
            j=0
            print(course,date)
            user=myClass.objects.all()
            serializer=myClassSerializers(user,many=True)
            for d in serializer.data:
                if d['course']==course and d['date']==date:
                    dic[j]=d
                    j=j+1
            return Response(dic)
        except :
            return Response("Date and course may not match !",status=status.HTTP_400_BAD_REQUEST)
