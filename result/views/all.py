from django.shortcuts import render,redirect
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import io
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import serializers
from result.models.first import Sem_first
from result.models.second import Sem_second
from result.models.third import Sem_third
from result.models.fourth import Sem_fourth
from result.models.fifth import Sem_fifth
from result.models.sixth import Sem_sixth
from result.serializers.result_serializers import *


class Result_All(APIView):
    def post(self, request, format=None):
        try:
            data=request.data
            rid=int(data.get('rid'))
            sem=int(data.get('semester'))
            if sem==1:
                user=Sem_first.objects.all()
                serializer=Sem_first_Serializers(user,many=True)
            elif sem==2:
                user=Sem_second.objects.all()
                serializer=Sem_second_Serializers(user,many=True)
            elif sem==3:
                user=Sem_third.objects.all()
                serializer=Sem_third_Serializers(user,many=True)
            elif sem==4:
                user=Sem_fourth.objects.all()
                serializer=Sem_fourth_Serializers(user,many=True)
            elif sem==5:
                user=Sem_fifth.objects.all()
                serializer=Sem_fifth_Serializers(user,many=True)
            elif sem==6:
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
                        if d['semester']==sem or d['rid']==rid:
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
            python_data=serializer.data
            obtain_marks=0
            dic={}
            j=0
            for d in python_data:
                for i in d:
                    if d['semester']==sem or d['rid']==rid:
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
    