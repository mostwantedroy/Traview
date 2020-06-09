from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import *
from django.db.models import Q

def test(request):
    cat = ["T0101", "T0102", "T0103", "T0201", "T0202", "T0203", "T0301", "T0302"]
    name_list = ["park_list", "mountain_list", "seashore_list", "history_list", "culture_list", "arch_list", "activity_list", "healing_list"]
    name_value = ["공원", "산", "연안", "역사", "문화", "건축", "활동", "힐링"]
    name_title = ["park_title", "mountain_title", "seashore_title", "history_title", "culture_title", "arch_title", "activity_list", "healing_title"]
    context = {}
    for i in range(8):
        context[name_title[i]] = name_value[i]
    for i in range(8):
        attraction = KeywordTable.objects.select_related('id').id.order_by('-num').filter(type__contains = cat[i])[:4]
        context[name_list[i]] = attraction

    return render(request, 'newsite/attraction_list.html', context)

def browse(request):
    context = {}
    cat_large = ['T01', 'T02', 'T03']
    cat_medium = ['T010', 'T020', 'T030']
    key_category = ['large', 'medium', 'small']
    for i in range(3):
        if i == 0:
            context[key_category[i]] = CodeDef.objects.all().filter(code__in = cat_large)
            # code_name, code
        elif i == 1:
            context[key_category[i]] = CodeTable.objects.all().filter(code__code__in = cat_large)
        else:
            context[key_category[i]] = CodeTable.objects.all().filter(code__code__contains = cat_medium[i])
            # detail_name , detail_code
    key_keyword = ['view', 'cost', 'valuation']
    view = [
        'thrill', 'skyscrapers', 'skyscraper', 'pretty', 'upper', 'wide', 'artistic', 'serene', 'ultra', 'worthy',
        'big', 'historical', 'magnificent', 'exotic', 'resting', 'colorful', 'gothic', 'extra', 'beauty', 'huge',
        'peaceful', 'spacious', 'extensive', 'expansive', 'affordable', 'vast', 'calm', 'smallish', 'crowded'
    ]
    cost = [
        'pricey', 'inexpensive', 'cheap', 'free', 'expensive', 'pricy', 'worthy', 'worth', 'overprised', 'overpriced',
        'reasonable', 'luxurious'
    ]
    valuation = [
        'extraordinary', 'tough', 'ideal', 'innovative', 'virtual', 'historic', 'reachable', 'quintessential', 'fantastic', 'pleasant', 'recommended', 'typical', 'eastern', 'impressive', 'reasonable', 'horrible', 'unique', 'psychedelic', 'wooden', 'incredible', 'trippy', 'thoughtful', 'vigorous', 'accessible', 'rare', 'hot', 'gorgeous', 'satisfied', 'awful', 'unbelievable', 'happy', 'local', 'unforgettable', 'photogenic', 'disappointed', 'friendly', 'modern', 'nice', 'ceremonial', 'archaeological', 'energetic', 'great', 'brilliant', 'convenient', 'romantic', 'approachable', 'disappointing', 'spectacular', 'wonderful', 'awesome', 'beautiful', 'popular', 'interactive', 'magical', 'historical', 'excellent', 'likely', 'special', 'weird', 'cheerful', 'peaceful', 'memorial', 'warm', 'futuristic', 'organized', 'interesting', 'glorious', 'confortable', 'enjoyable', 'stimulating', 'young', 'picturesque', 'manicured', 'traditional', 'lovely', 'understated', 'famous', 'funny', 'recommend', 'exotic', 'instagramable', 'amazing', 'foggy', 'walkable', 'dirt', 'diverse', 'best', 'stunning', 'renowned', 'breathtaking', 'fun'
    ]
    value_keyword = [view, cost, valuation]
    for i in range(3):
        context[key_keyword[i]] = value_keyword[i]
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