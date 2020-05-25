from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import Attraction

def index(request):
    attraction_list = Attraction.objects.order_by('name')
    context = {'attraction_list' : attraction_list}
    return render(request, 'newsite/attraction_list.html', context)

def poster(Attraction):
    Attraction.objects.order_by('num')




# Defining REST API from this line.

from rest_framework import viewsets
from .serializers import AttractionSerializer

class AttractionViewSet(viewsets.ModelViewSet):
    queryset = Attraction.objects.all()
    serializer_class = AttractionSerializer
