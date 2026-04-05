from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver
import os

class Categorie(models.Model):
    nom = models.CharField(verbose_name="nom categorie", max_length=100)

    def __str__(self):
        return f"{self.nom}"

STATUS = ((0, "Brouillon"), (1, "Publier"))

class Article(models.Model):
    titre=models.CharField(verbose_name="Titre de l'article", max_length=100, unique=True)
    slug=models.SlugField(verbose_name="numero slug", max_length=100, unique=True)
    contenu=models.TextField(verbose_name="contenu articles")
    image=models.ImageField(verbose_name="image", upload_to="articles/", blank=True, null=True)
    statut= models.IntegerField(verbose_name="status article", choices=STATUS, default=0)
    date_creation= models.DateField(verbose_name="date creation", auto_now=False, auto_now_add=False)
    date_publication=models.DateField(verbose_name="date publication", auto_now=False, auto_now_add=True)
    user = models.ForeignKey(User, verbose_name="Utilisateurs", on_delete=models.CASCADE)
    categorie=models.ForeignKey(Categorie, verbose_name="categorie article", on_delete=models.CASCADE)
    
    def save(self, *args, **kwargs):
    
        if not self.slug:
            self.slug = slugify(self.titre)
        super().save(*args, **kwargs)
        
    class Meta:
        ordering = ['-date_publication']


    def __str__(self):
        return f"{self.titre}- {self.slug}"

class Commentaire(models.Model):
    message=models.TextField(verbose_name="message commentaire")
    date_publication = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    def __str__(self):
        return self.message
    

# Supprimer le fichier image associé lors de la suppression de l'article
@receiver(pre_delete, sender=Article)
def delete_post_image(sender, instance, **kwargs):
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)