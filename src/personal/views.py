from django.shortcuts import render
from django.db.models import Q
from operator import attrgetter
from itertools import chain
from django.views.generic.list import ListView
from yomex.models import WristWatch,Perfume,Shoes,Glass



def home_view(request):
    context={}
    # watch batch 1
    wristwatch=WristWatch.objects.all()[0:3]
    context['wristwatch'] = wristwatch 


    wrist=WristWatch.objects.all()[3:]
    context['wrist'] = wrist

    return render(request,'personal/home.html',context=context)


def search_results(request):
    context = {}
    query = request.GET.get('q')
    wristwatch = WristWatch.objects.filter(Q(name__icontains=query)| Q(description__icontains=query)).distinct()
    shoes=Shoes.objects.filter(Q(name__icontains=query) | Q(description__icontains=query)).distinct()
    queryset=list(chain(wristwatch,shoes))
    context['query'] = query
    context['queryset'] =  queryset
    return render(request,'personal/search.html',context=context)

       
