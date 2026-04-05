from django.contrib import admin

from .models import *

# Register your models here.

@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display=('nom',)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display=('titre','statut','date_creation','user','categorie')


@admin.register(Commentaire)
class CommentaireAdmin(admin.ModelAdmin):
    list_display=('date_publication','user','article')