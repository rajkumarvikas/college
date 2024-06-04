from users.models.registration import User_Model
from rest_framework import serializers

class faculty_login(serializers.ModelSerializer):
    class Meta:
        model=User_Model
        fields=['id','registration_id','college_id']

    def create(self, validated_data):
        return User_Model.objects.create(**validated_data)