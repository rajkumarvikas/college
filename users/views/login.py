from django.shortcuts import render,redirect
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from users.models.address import Address_Model
from users.models.document import Document_model
from users.models.Document_urls import Document_Url
from users.models.personalDetails import Personal_Details
from users.models.qualification import Qualifications_model
from users.models.registration import User_Model
from users.serializers.address import Address_Serializers
from users.serializers.document import Document_Serializers
from users.serializers.document_urls import Document_url_Serializers
from users.serializers.personalDetails import Persona_Details_Serializers
from users.serializers.qualification import Qualification_Serializers
from users.serializers.registration import User_Serializers
from payment.models import Payement
from payment.serializers import PaymentSerializers
import random
import io
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.contrib.auth.hashers import make_password,check_password
from rest_framework.decorators import api_view


def pay(pk):
    try:
        user1=Payement.objects.get(rid=pk)
        serializer1=PaymentSerializers(user1)
        python_data1=serializer1.data
        pay=python_data1['pay']
        return pay
    except:
         return "false"

class Login_View(APIView):
        def post(self, request, format=None):
            try:
                json_data=request.body
                stream=io.BytesIO(json_data)
                python_data=JSONParser().parse(stream)
                email=python_data.get('email')
                if email=='' or email==None:
                     return Response("Email is required",status=status.HTTP_404_NOT_FOUND)
                password=python_data.get('password')
                if password=='' or password==None :
                     return Response("Password is required ",status=status.HTTP_401_UNAUTHORIZED)
                user=User_Model.objects.all()
                serializer=User_Serializers(user,many=True)
                em=serializer.data
                m=0
                for j in em:
                     if email==j['email']:
                          m=1
                if m==0:
                     return Response("Email not exits")
                
                k=0
                for i in em:
                     if email==i['email'] and check_password(password,i['password']):
                         record=i['id']
                         k=1
                         break
                if k==0:
                     return Response("user id or password not matching ",status=status.HTTP_401_UNAUTHORIZED)
                else:
                    pk=record
                    user=User_Model.objects.get(pk=pk)
                    serializer=User_Serializers(user)
                    python_data=serializer.data
                    registration_id=python_data['registration_id']
                    course=python_data['course']
                    first_name=python_data['first_name']
                    middle_name=python_data['middle_name']
                    last_name=python_data['last_name']
                    role=python_data['role']
                    if role=="faculty":
                         data="can't login in student view"
                         return Response("can't login in student view",status=status.HTTP_401_UNAUTHORIZED)
                    phone=python_data['phone']
                    email=python_data['email']

                    
                    data={
                         'id':pk,
                         'registration_id':registration_id,
                         'course':course,
                         'first_name':first_name,
                         'middle_name':middle_name,
                         'last_name':last_name,
                         'role':role,
                         'phone':phone,
                         'email':email
                    }
                    user=Personal_Details.objects.get(rid=pk)
                    serializer=Persona_Details_Serializers(user)
                    python_data=serializer.data
                    father_name=python_data['father_name']
                    mother_name=python_data['mother_name']
                    sex=python_data['sex']
                    cast=python_data['cast']
                    dob=python_data['dob']
                    nationality=python_data['nationality']

                    data={
                         'id':pk,
                         'registration_id':registration_id,
                         'first_name':first_name,
                         'middle_name':middle_name,
                         'last_name':last_name,
                         'role':role,
                         'phone':phone,
                         'email':email,
                         'father_name':father_name,
                         'mother_name':mother_name,
                         'sex':sex,
                         'cast':cast,
                         'dob':dob,
                         'nationality':nationality}

                    user=Address_Model.objects.get(rid=pk)
                    serializer=Address_Serializers(user)
                    python_data=serializer.data
                    building_number=python_data['building_number']
                    locality=python_data['locality']
                    sublocality=python_data['sublocality']
                    state=python_data['state']
                    district=python_data['district']
                    pincode=python_data['pincode']
                    contract_number=python_data['contract_number']
                    alternate_number=python_data['alternate_number']
                    data={
                         'id':pk,
                         'registration_id':registration_id,
                         'first_name':first_name,
                         'middle_name':middle_name,
                         'last_name':last_name,
                         'role':role,
                         'phone':phone,
                         'email':email,
                         'father_name':father_name,
                         'mother_name':mother_name,
                         'sex':sex,
                         'cast':cast,
                         'dob':dob,
                         'nationality':nationality,
                         'building_number':str(building_number),
                         'locality':locality,
                         'sublocality':sublocality,
                         'state':state,
                         'district':district,
                         'pincode':pincode,
                         'contract_number':contract_number,
                         'alternate_number':alternate_number}

                    user=Qualifications_model.objects.get(rid=pk)
                    serializer=Qualification_Serializers(user)
                    python_data=serializer.data
                    status1=python_data['status']
                    year=python_data['year']
                    school=python_data['school']
                    roll_code=python_data['roll_code']
                    total_marks=python_data['total_marks']
                    obtain_marks=python_data['obtain_marks']

                    data={
                         'id':pk,
                         'registration_id':registration_id,
                         'first_name':first_name,
                         'middle_name':middle_name,
                         'last_name':last_name,
                         'role':role,
                         'phone':phone,
                         'email':email,
                         'father_name':father_name,
                         'mother_name':mother_name,
                         'sex':sex,
                         'cast':cast,
                         'dob':dob,
                         'nationality':nationality,
                         'building_number':str(building_number),
                         'locality':locality,
                         'sublocality':sublocality,
                         'state':state,
                         'district':district,
                         'pincode':pincode,
                         'contract_number':contract_number,
                         'alternate_number':alternate_number,
                         'status':status1,
                         'year':year,
                         'school':school,
                         'roll_code':roll_code,
                         'total_marks':total_marks,
                         'obtain_marks':obtain_marks}

                    user=Document_Url.objects.get(rid=pk)
                    serializer=Document_url_Serializers(user)
                    python_data=serializer.data
                    photo=python_data['photo_url']
                    signatue=python_data['signatue_url']
                    adhar=python_data['adhar_url']
                    tenth=python_data['tenth_url']
                    twelth=python_data['twelth_url']
                    data={
                         'id':pk,
                         'registration_id':registration_id,
                         'first_name':first_name,
                         'middle_name':middle_name,
                         'last_name':last_name,
                         'role':role,
                         'phone':phone,
                         'email':email,
                         'father_name':father_name,
                         'mother_name':mother_name,
                         'sex':sex,
                         'cast':cast,
                         'dob':dob,
                         'nationality':nationality,
                         'building_number':str(building_number),
                         'locality':locality,
                         'sublocality':sublocality,
                         'state':state,
                         'district':district,
                         'pincode':pincode,
                         'contract_number':contract_number,
                         'alternate_number':alternate_number,
                         'status':status1,
                         'year':year,
                         'school':school,
                         'roll_code':roll_code,
                         'total_marks':total_marks,
                         'obtain_marks':obtain_marks,
                         'photo':photo,
                         'signature':signatue,
                         'adhar':adhar,
                         'tenth':tenth,
                         'twelth':twelth,
                         'pay':pay(pk),

                    }
                    return Response(data)
                
            except:
                return Response(data)