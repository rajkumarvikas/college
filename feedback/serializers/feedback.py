from feedback.models.feedback import Model_Feedback
from rest_framework import serializers

class Serializers_Feedback(serializers.ModelSerializer):
    class Meta:
        model=Model_Feedback
        fields="__all__"