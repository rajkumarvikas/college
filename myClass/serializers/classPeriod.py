from rest_framework import serializers
from myClass.models.classPeriod import myClass

class myClassSerializers(serializers.ModelSerializer):
    class Meta:
        model=myClass
        fields=['id',
                'faculty_name',
                'date',
                'start',
                'end',
                'course',
                'description'
        ]