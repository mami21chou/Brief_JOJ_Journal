from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Commentaire, Article
from django.contrib.auth.models import User

from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver
import os

@receiver(post_save, sender=Commentaire)
def envoyer_email_commentaire(sender, instance, created, **kwargs):
    if created:
        # recuperer les admins
        admins = User.objects.filter(is_staff=True)

        emails = []
        # recuperer l'email de chaque admin le mettre dans la liste
        for admin in admins:
            if admin.email:
                emails.append(admin.email)
                
        send_mail(
            subject="Nouveau commentaire recu",
            message=f"""
            Un nouveau commentaire est en attente de lecture.

            Article : {instance.article.titre}
            Auteur : {instance.user}
            Message : {instance.message}
            """,
            from_email="joj@gmail.com",
            recipient_list=["adminjoj@gmail.com"], # emails
            fail_silently=True
        )
        

# Supprimer le fichier image associé lors de la suppression de l'article
@receiver(pre_delete, sender=Article)
def delete_post_image(sender, instance, **kwargs):
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)