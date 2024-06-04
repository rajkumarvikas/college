from rest_framework import serializers
from users.models.Document_urls import Document_Url

    

class Document_url_Serializers(serializers.ModelSerializer):
    class Meta:
        model=Document_Url
        fields="__all__"

    def create(self, validated_data):
        return Document_Url.objects.create(**validated_data)