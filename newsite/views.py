from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import Attraction

from rest_framework import viewsets
from .serializers import AttractionSerializer

def index(request):
    attraction_list = Attraction.objects.order_by('name')
    context = {'attraction_list' : attraction_list}
    return render(request, 'newsite/attraction_list.html', context)

class AttractionViewSet(viewsets.ModelViewSet):
    queryset = Attraction.objects.all()
    serializer_class = AttractionSerializer

