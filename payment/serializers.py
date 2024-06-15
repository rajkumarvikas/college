from .models import Payement
from rest_framework import serializers

class PaymentSerializers(serializers.ModelSerializer):
    class Meta:
        model=Payement
        fields="__all__"