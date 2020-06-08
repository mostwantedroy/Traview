from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import *
from django.db.models import Q

def browse(request):
    context = {}
    cat1 = ["인문", "자연", "레저"]
    cat2 = ["공원", "산", "연안", "역사", "문화", "건축", "활동", "힐링"]
    cat3 = []
    keyword = ["무드", "비용", "평가"]
    return render(request, 'newsite/browse_page.html', context)

def poster(request):
    cat = ["T0101", "T0102", "T0103", "T0201", "T0202", "T0203", "T0301", "T0302"]
    name_list = ["park_list", "mountain_list", "seashore_list", "history_list", "culture_list", "arch_list", "activity_list", "healing_list"]
    name_value = ["공원", "산", "연안", "역사", "문화", "건축", "활동", "힐링"]
    name_title = ["park_title", "mountain_title", "seashore_title", "history_title", "culture_title", "arch_title", "activity_list", "healing_title"]
    context = {}
    for i in range(8):
        context[name_title[i]] = name_value[i]
    for i in range(8):
        attraction = AttTable.objects.order_by('-num').filter(type__contains = cat[i])[:4]
        context[name_list[i]] = attraction

    return render(request, 'newsite/attraction_list.html', context)

# Defining REST API from this line.

from rest_framework import viewsets
from .serializers import *

class AttractionViewSet(viewsets.ModelViewSet):
    queryset = KeywordTable.objects.all().select_related('id')
    serializer_class = KeywordSerializer

class CodeViewSet(viewsets.ModelViewSet):
    queryset = CodeTable.objects.all()
    serializer_class = CodeSerializer