from django.shortcuts import render,redirect
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from result.models.sixth import Sem_sixth
from result.serializers.result_serializers import Sem_sixth_Serializers
import io
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser


class Sem_sixth_Views(APIView):
    def get(self, request,rid=None, format=None):
       try:
            user=Sem_sixth.objects.all()
            serializer=Sem_sixth_Serializers(user,many=True)
            python_data=serializer.data
            obtain_marks=0
            dic={}
            dic[0]={
                "rid":rid
            }
            j=0
            for d in python_data:
                for i in d:
                    if d['semester']==6 or d['rid']==rid:
                        obtain_marks=obtain_marks+d['total_obtain']
                        d={
                            "project_name":d["project_name"],
                            "seminar_presentation":d["seminar_presentation"],
                            "viva_voce":d["viva_voce"],
                        }
                        j=j+1
                        dic[j]=d
                        break
            dic[j+1]={"total_marks":obtain_marks}
            return Response(dic)
       except :
           return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)