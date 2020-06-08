from rest_framework import serializers
from .models import *

class AttractionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttTable
        fields = ('name', 'id', 'star', 'num', 'type','address', 'lat', 'lon', 'location_code', 'image')

class CodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CodeTable
        fields = ('detail_code', 'detail_name', 'code', 'detail')

class KeywordSerializer(serializers.ModelSerializer):
    class Meta:
        model = KeywordTable
        fields = ('id', 'valuation', 'view', 'cost', 'total')