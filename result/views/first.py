from django.shortcuts import render,redirect
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from result.models.first import Sem_first
from result.serializers.result_serializers import Sem_first_Serializers
import io
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser


class Sem_first_Views(APIView):
    def get(self, request,rid=None, format=None):
       try:
            user=Sem_first.objects.all()
            serializer=Sem_first_Serializers(user,many=True)
            python_data=serializer.data
            obtain_marks=0
            dic={}
            dic[0]={
                "rid":rid
            }
            j=0
            for d in python_data:
                for i in d:
                    if d['semester']==1 or d['rid']==rid:
                        d={
                            "paper_code":d["paper_code"],
                            "paper_title":d["paper_title"],
                            "internal_marks":d["internal_marks"],
                            "external_marks":d["external_marks"],
                            "obtain_marks":d["obtain_marks"],
                        }
                        obtain_marks=obtain_marks+d['obtain_marks']
                        j=j+1
                        dic[j]=d
                        break
            dic[j+1]={"total_marks":obtain_marks}
            return Response(dic)
       except :
           return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    