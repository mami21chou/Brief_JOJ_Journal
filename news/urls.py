from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from .views import InscriptionView
from django.urls import path
from django.contrib.auth import views as auth_views
from .forms import CustomLoginForm

urlpatterns = [
    path('inscription/' , InscriptionView.as_view(), name='inscription'),
    path(
        'login/',
        auth_views.LoginView.as_view(
            template_name='login.html',
            authentication_form=CustomLoginForm
        ),
        name='login'
    ),
    
    # path('connexion/', auth_views.LoginView.as_view(authentication_form=CustomLoginForm, template_name='login.html'),  name='login'),
    path('deconnexion', LogoutView.as_view(), name='logout'),
    
    
    path('', views.home, name='home'),
    path('articles/', views.liste_article, name='liste_article'),
    path('article/<int:id>/detail', views.detail_article, name='detail_article'),
    path('article/<int:id>/modifier_commentaire', views.modifier_commentaire, name='modifier_commentaire'),
    path('article/<int:id>/supprimer_commentaire', views.supprimer_commentaire, name='supprimer_commentaire'),
]