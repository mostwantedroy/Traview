from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import AttTable
from django.db.models import Q

def index(request):
    attraction_list = AttTable.objects.order_by('num')
    context = {'attraction_list' : attraction_list}
    return render(request, 'newsite/attraction_list.html', context)

def poster(request):
    cat = ["T0101", "T0102", "T0103", "T0201", "T0202", "T0203", "T0301", "T0302"]
    name = ["공원", "산", "연안", "역사", "문화", "건축", "활동", "힐링"]
    context = {}
    for i in len(cat):
        attraction = AttTable.objects.order_by('-num').filter(type__in = cat[i])
        context[name[i]] = attraction
    return render(request, 'newsite/attraction_list.html', context)

# Defining REST API from this line.

from rest_framework import viewsets
from .serializers import AttractionSerializer

class AttractionViewSet(viewsets.ModelViewSet):
    queryset = AttTable.objects.filter(star = 50)
    serializer_class = AttractionSerializer