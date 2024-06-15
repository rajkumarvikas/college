from .models import Payement
from .serializers import PaymentSerializers
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class Payment_views(APIView):
    def post(self, request, format=None):
        serializer = PaymentSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Payment Successfully", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)