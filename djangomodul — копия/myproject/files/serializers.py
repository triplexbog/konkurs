from rest_framework import serializers
from .models import File

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        
        model = File
        fields = ['file_id', 'name', 'file', 'owner', 'shared_with']
        read_only_fields = ['file_id', 'owner']


class FileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ['name']
