from rest_framework import serializers
from .models import Chat_Data


class ChatDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat_Data
        fields = '__all__'