from django.urls import path
from .views import home,news_detail

urlpatterns = [
    path('', home, name='home'),
    path('news_detail/<int:pk>', news_detail, name='news_detail'), 
]