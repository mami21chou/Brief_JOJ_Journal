from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Commentaire
from django.contrib.auth.models import User

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