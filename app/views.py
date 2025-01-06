from django.shortcuts import render,get_object_or_404
from .models import Yangiliklar

def home(request):
    latest_post = Yangiliklar.objects.all().order_by('-date')[:1]
    other_posts = Yangiliklar.objects.all().order_by('-date')[1:5]
    return render(request, 'home.html', {'latest_post': latest_post, 'other_posts': other_posts})

def news_detail(request, pk):
    new = get_object_or_404(Yangiliklar, pk=pk)
    return render(request, 'news/detail.html', {'new': new})