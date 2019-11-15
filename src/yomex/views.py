from django.shortcuts import render,get_object_or_404
from . models import WristWatch,Perfume,Shoes,Glass

def view_wristwatch(request):
    context={}
    wristwatches=WristWatch.objects.all()
    context['wristwatches']=wristwatches
    return render(request,'yomex/watch.html',context=context)


def detail_wristwatch_view(request,slug):
    context ={}
    watch = get_object_or_404(WristWatch,slug=slug)
    context['watch'] = watch
    return render(request,'yomex/detail_watch.html',context=context)



def view_shoe(request):
    context ={}
    shoes = Shoes.objects.all()
    context['shoes']=shoes
    return render(request,'yomex/shoe.html',context=context)


def detail_shoe_view(request,slug):
    context ={}
    shoe = get_object_or_404(Shoes,slug=slug)
    context['shoe'] = shoe
    return render(request,'yomex/detail_shoe.html',context=context)

