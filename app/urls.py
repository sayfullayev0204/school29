from django.urls import path
from .views import home,news_detail,about_school,leadership,news,olimpiada

urlpatterns = [
    path('', home, name='home'),
    path('news_detail/<int:pk>', news_detail, name='news_detail'), 
    path('about-school/', about_school, name='about_school'), 
    path('leadership/', leadership, name='leadership'), 
    path('news/', news, name='news'),  
    path('olimpiada/', olimpiada, name='olimpiada'),
]