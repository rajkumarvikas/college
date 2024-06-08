from rest_framework import serializers
from myClass.models.classPeriod import myClass

class myClassSerializers(serializers.ModelSerializer):
    date = serializers.DateField(
        format='%d/%m/%Y',  # format for output
        input_formats=['%d/%m/%Y']  # format for input
    )
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