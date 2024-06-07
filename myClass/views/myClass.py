from myClass.models.classPeriod import myClass
from myClass.serializers.classPeriod import myClassSerializers
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class myClassView(APIView):
    def get(self, request, format=None):
        try:
            data=request.data
            cr=data.get('course')
            course=cr.upper()
            date=data.get('date')
            dic={}
            j=0
            user=myClass.objects.all()
            serializer=myClassSerializers(user,many=True)
            for d in serializer.data:
                if d['course']==course and d['date']==date:
                    dic[j]=d
                    j=j+1
            return Response(dic)
        except :
            return Response("Date and course may not match !",status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, format=None):
        python_data=request.data 
        fn=python_data.get('faculty_name')
        pd=python_data.get('date')
        ps=python_data.get('start')
        pe=python_data.get('end')
        cr=python_data.get('course')
        ds=python_data.get('description')
        model_data=myClass.objects.filter(faculty_name=fn,date=pd,start=ps,end=pe,course=cr,description=ds)
        if model_data.exists():
            return Response("Record Save already",status=status.HTTP_400_BAD_REQUEST)
        serializer = myClassSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Record Save Successfully", status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def delete(self,request,pk=None,format=None):
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
