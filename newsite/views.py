from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import AttTable

def index(request):
    attraction_list = AttTable.objects.order_by('num')
    context = {'attraction_list' : attraction_list}
    return render(request, 'newsite/attraction_list.html', context)

def poster(AttTable):
    middle = []
    for cat in middle:
        attraction_list = AttTable.objects.filter(middle = cat).order_by('num').order_by('star')




# Defining REST API from this line.

from rest_framework import viewsets
from .serializers import AttractionSerializer

class AttractionViewSet(viewsets.ModelViewSet):
    queryset = AttTable.objects.all()
    serializer_class = AttractionSerializer