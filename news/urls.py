
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('articles/', views.liste_artciles, name='liste_article'),
    path('article/detail', views.detail_article, name='detail_article'),
]
