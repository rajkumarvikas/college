from result.models.first import Sem_first
from result.models.second import Sem_second
from result.models.third import Sem_third
from result.models.fourth import Sem_fourth
from result.models.fifth import Sem_fifth
from result.models.sixth import Sem_sixth
from rest_framework import serializers

class Sem_first_Serializers(serializers.ModelSerializer):
    class Meta:
        model=Sem_first
        fields="__all__"
class Sem_second_Serializers(serializers.ModelSerializer):
    class Meta:
        model=Sem_second
        fields="__all__"
class Sem_third_Serializers(serializers.ModelSerializer):
    class Meta:
        model=Sem_third
        fields="__all__"
class Sem_fourth_Serializers(serializers.ModelSerializer):
    class Meta:
        model=Sem_fourth
        fields="__all__"
class Sem_fifth_Serializers(serializers.ModelSerializer):
    class Meta:
        model=Sem_fifth
        fields="__all__"
class Sem_sixth_Serializers(serializers.ModelSerializer):
    class Meta:
        model=Sem_sixth
        fields="__all__"