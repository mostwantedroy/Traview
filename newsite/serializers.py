from rest_framework import serializers
from .models import AttTable

class AttractionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttTable
        fields = ('name', 'star', 'num')