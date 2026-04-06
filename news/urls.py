from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from .views import InscriptionView
from django.urls import path

urlpatterns = [
    path('inscription/' , InscriptionView.as_view(), name='inscription'),
         
    path('connexion/', LoginView.as_view(),  name='login'),
    path('deconnexion', LogoutView.as_view(), name='logout'),
    
    
    path('', views.home, name='home'),
    
    path('articles/', views.liste_article, name='liste_article'),
    path('article/<int:id>/detail', views.detail_article, name='detail_article'),
    path('article/<int:id>/modifier_commentaire', views.modifier_commentaire, name='modifier_commentaire'),
    path('article/<int:id>/supprimer_commentaire', views.supprimer_commentaire, name='supprimer_commentaire'),
]