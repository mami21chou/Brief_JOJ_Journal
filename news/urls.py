from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from .views import InscriptionView
from django.urls import path

urlpatterns = [
    path('inscription/' , InscriptionView.as_view(), name='inscription'),
    path('connexion/', LoginView.as_view(), name='login'),
    path('deconnexion', LogoutView.as_view(), name='logout'),
     path('', views.home, name='home'),
    path('articles/', views.liste_artciles, name='liste_article'),
    path('article/detail', views.detail_article, name='detail_article'),
]