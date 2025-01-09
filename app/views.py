from django.shortcuts import render,get_object_or_404
from .models import Yangiliklar,Olimpiada
import re

def extract_youtube_id(url):
    """Extracts the YouTube video ID from a given URL."""
    match = re.search(r'(?:v=|\/)([0-9A-Za-z_-]{11})', url)
    return match.group(1) if match else None


def home(request):
    latest_post = Yangiliklar.objects.all().order_by('-date')[:1]
    other_posts = Yangiliklar.objects.all().order_by('-date')[1:5]
    
    return render(request, 'home.html', {'latest_post': latest_post, 'other_posts': other_posts})

def news_detail(request, pk):
    new = get_object_or_404(Yangiliklar, pk=pk)
    return render(request, 'detail.html', {'new': new})

def about_school(request):
    return render(request, 'about_school.html')

def leadership(request):
    return render(request, 'leadership.html')

def news(request):
    news_list = Yangiliklar.objects.all().order_by('-date')
    return render(request, 'news.html', {'news_list': news_list})

def olimpiada(request):
    olimpiada = Olimpiada.objects.all()
    return render(request, 'olimpiada.html', {'olimpiada': olimpiada})