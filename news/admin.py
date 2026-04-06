from django.contrib import admin

from .models import *

@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display=('nom',)
    search_fields = ['nom']


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display=('titre','statut','date_creation','user','categorie')
    list_filter = ('statut', 'categorie')
    search_fields = ['titre', 'contenu']


@admin.register(Commentaire)
class CommentaireAdmin(admin.ModelAdmin):
    list_display=('message', 'date_publication','user','article')
    list_filter = ('article',)
    search_fields = ['message', 'article']