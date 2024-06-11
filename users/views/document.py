from django.shortcuts import render,redirect
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from users.models.document import *
from users.serializers.document import Document_Serializers
from users.serializers.document_urls import Document_url_Serializers
import io
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
import requests



api_token = '620475f529a9036435425c686eed9774914ed0c9'
username = 'Arkas'
upload_path = '/home/Arkas/documents/'
def Upload_Url(u):
    print(u)
    url="home/Arkas/college"+str(u)
    return url

class Document_View(APIView):
    def get(self, request,pk=None, format=None):
        try:
            if pk is not None:
                user=Document_model.objects.get(pk=pk)
            else:
                user=Document_model.objects.all()
        except Document_model.DoesNotExist:
            return Response("Data not found",status=status.HTTP_404_NOT_FOUND)
        if pk is not None:
            serializer=Document_Serializers(user)
        else:
            serializer=Document_Serializers(user,many=True)
            print(serializer.data)
        return Response(serializer.data)
        return Response("Data not found",status=status.HTTP_400_BAD_REQUEST)
    def post(self,request,format=None):
        try:
            python_data=request.data
            rid=python_data.get('rid')
            user=Document_model.objects.filter(rid=rid)
            if user.exists():
                return Response("Document upload  already",status=status.HTTP_400_BAD_REQUEST)
            python_data=request.data
            rid=python_data.get('rid')
            if rid=='' or rid==None:
                return Response("registration rid required",status=status.HTTP_204_NO_CONTENT)
            photo=python_data.get('photo')
            signatue=python_data.get('signatue')
            adhar=python_data.get('adhar')
            tenth=python_data.get('tenth')
            twelth=python_data.get('twelth')
            python_data={
                'photo':photo,
                'signatue':signatue,
                'adhar':adhar,
                'tenth':tenth,
                'twelth':twelth,
            }

            # updating code here...........
            responseData =[]
            
            for doc in python_data :
                response = requests.post(
                    url=f'https://www.pythonanywhere.com/api/v0/user/{username}/files/path/{upload_path}/{rid}/{python_data[doc]}',
                    headers={'Authorization': f'Token {api_token}'},
                    files={'content': ('photo.jpg', python_data[doc].read())}
                )
                if response.status_code >= 200 or response.status_code <=300:
                    print(response.url)
                    print('File uploaded successfully')
                else:
                    print(f'Failed to upload file: {response.status_code}, {response.text}')
                responseData.append(response.url)

            python_data1={
                'rid':rid,
                'photo_url':responseData[0],
                'signatue_url':responseData[1],
                'adhar_url':responseData[2],
                'tenth_url':responseData[3],
                'twelth_url':responseData[4]
            }
            seri=Document_url_Serializers(data=python_data1)
            if seri.is_valid():
                seri.save()
                return Response(responseData,status=status.HTTP_201_CREATED)
            else:
                return Response("Error while uploading file !",status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Document_model.DoesNotExist:
            return Response("Field not exits",status=status.HTTP_400_BAD_RESQUEST)
        return Response(seri.errors,status=status.HTTP_400_BAD_REQUEST)
    def put(self,request,pk=None,format=None):
        try:
            user=Document_model.objects.get(pk=pk)
            ri=Document_Serializers(user)
            python_data=request.data
            rid=python_data.get('rid')
            photo=python_data.get('photo')
            signatue=python_data.get('signatue')
            adhar=python_data.get('adhar')
            tenth=python_data.get('tenth')
            twelth=python_data.get('twelth')
            python_data={
                'rid':rid,
                'photo':photo,
                'signatue':signatue,
                'adhar':adhar,
                'tenth':tenth,
                'twelth':twelth
            }
            serializer=Document_Serializers(user,data=python_data)
            if serializer.is_valid():
                serializer.save()
                return Response("Document uploaded successfully",status=status.HTTP_201_CREATED)
        except Document_model.DoesNotExist:
            return Response("Field not found",status=status.HTTP_400_BAD_RESQUEST)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk=None,format=None):
        try:
            if pk==None:
                return Response(status=status.HTTP_404_NOT_FOUND)
            else:
                user=Document_model.objects.get(pk=pk)
        except Document_model.DoesNotExist:
            return Response("Data not exits",status=status.HTTP_404_NOT_FOUND)
        user.delete()
        return Response("Documents deleted successfully",status=status.HTTP_204_NO_CONTENT)
