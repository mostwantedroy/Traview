from rest_framework import serializers
from .models import AttTable1

class AttractionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttTable1
        fields = ('name', 'star', 'main', 'middle', 'type', 'image')