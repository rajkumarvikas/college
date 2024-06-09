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
            res={}
            dic1={}
            j=0
            user=Sem_first.objects.all()
            serializer=Sem_first_Serializers(user,many=True)
            python_data=serializer.data
            obtain_marks=0
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
                        dic1[j]=d
                        break
            j=j+1
            dic1[j]={"total_marks":obtain_marks}
            dic2={}
            j=0
            user=Sem_second.objects.all()
            serializer=Sem_second_Serializers(user,many=True)
            python_data=serializer.data
            obtain_marks=0
            for d in python_data:
                for i in d:
                    if d['semester']==2 or d['rid']==rid:
                        d={
                            "paper_code":d["paper_code"],
                            "paper_title":d["paper_title"],
                            "internal_marks":d["internal_marks"],
                            "external_marks":d["external_marks"],
                            "obtain_marks":d["obtain_marks"],
                        }
                        obtain_marks=obtain_marks+d['obtain_marks']
                        j=j+1
                        dic2[j]=d
                        break
            j=j+1
            dic2[j]={"total_marks":obtain_marks}
            dic3={}
            j=0
            user=Sem_third.objects.all()
            serializer=Sem_third_Serializers(user,many=True)
            python_data=serializer.data
            obtain_marks=0
            for d in python_data:
                for i in d:
                    if d['semester']==3 or d['rid']==rid:
                        d={
                            "paper_code":d["paper_code"],
                            "paper_title":d["paper_title"],
                            "internal_marks":d["internal_marks"],
                            "external_marks":d["external_marks"],
                            "obtain_marks":d["obtain_marks"],
                        }
                        obtain_marks=obtain_marks+d['obtain_marks']
                        j=j+1
                        dic3[j]=d
                        break
            j=j+1
            dic3[j]={"total_marks":obtain_marks}
            dic4={}
            j=0
            user=Sem_fourth.objects.all()
            serializer=Sem_fourth_Serializers(user,many=True)
            python_data=serializer.data
            obtain_marks=0
            for d in python_data:
                for i in d:
                    if d['semester']==4 or d['rid']==rid:
                        d={
                            "paper_code":d["paper_code"],
                            "paper_title":d["paper_title"],
                            "internal_marks":d["internal_marks"],
                            "external_marks":d["external_marks"],
                            "obtain_marks":d["obtain_marks"],
                        }
                        obtain_marks=obtain_marks+d['obtain_marks']
                        j=j+1
                        dic4[j]=d
                        break
            j=j+1
            dic4[j]={"total_marks":obtain_marks}
            dic5={}
            j=0
            user=Sem_fifth.objects.all()
            serializer=Sem_fifth_Serializers(user,many=True)
            python_data=serializer.data
            obtain_marks=0
            for d in python_data:
                for i in d:
                    if d['semester']==5 or d['rid']==rid:
                        d={
                            "paper_code":d["paper_code"],
                            "paper_title":d["paper_title"],
                            "internal_marks":d["internal_marks"],
                            "external_marks":d["external_marks"],
                            "obtain_marks":d["obtain_marks"],
                        }
                        obtain_marks=obtain_marks+d['obtain_marks']
                        j=j+1
                        dic5[j]=d
                        break
            j=j+1
            dic5[j]={"total_marks":obtain_marks}
            dic6={}
            j=0
            user=Sem_sixth.objects.all()
            serializer=Sem_sixth_Serializers(user,many=True)
            python_data=serializer.data
            obtain_marks=0
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
                        dic6[j]=d
                        break
            j=j+1
            dic6[j]={"total_marks":obtain_marks}
            res={
                'sem1':dic1,
                'sem2':dic2,
                'sem3':dic3,
                'sem4':dic4,
                'sem5':dic5,
                'sem6':dic6
                }
            return Response(res)
        except :
           return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    