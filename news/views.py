from django.shortcuts import render,get_object_or_404, redirect
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from .forms import CommentaireForm
from django.contrib.auth.decorators import login_required


class InscriptionView(CreateView):
    form_class=UserCreationForm
    template_name='registration/inscription.html'
    success_url= reverse_lazy('login')



def home(request):
    # Récuperer les trois articles les plus recents
    articles = Article.objects.filter(statut=1).order_by('-date_publication')[:3]
    return render(request, 'index.html', {'articles': articles})


def liste_article(request):
    
    # Catégorie selectionné
    categorie_filtre = request.GET.get('categorie')
    
    # Filtrer par catégorie
    if categorie_filtre:
        articles = Article.objects.filter(categorie__nom=categorie_filtre).order_by('-date_publication')
        
    else:
        articles=Article.objects.filter(statut=1).order_by('-date_publication')
        
    # Récuperer tout les catégories
    categories = Categorie.objects.all()
    
    context = {
        'categories': categories,
        'articles':articles,
        'categorie_active': categorie_filtre,
    }
    
    return render(request, 'article_list.html',context)



def  detail_article(request,id):
    
    # recuper l'article
    article=get_object_or_404(Article,pk=id)
    
    # récuper les commentaires associé à l'article
    commentaires = Commentaire.objects.filter(article=article).order_by('-date_publication')
    
    form = CommentaireForm()

    # ajout commentaire
    if request.method == "POST":
        if request.user.is_authenticated:
            form = CommentaireForm(request.POST)
            if form.is_valid():
                commentaire = form.save(commit=False)
                commentaire.user = request.user
                commentaire.article = article
                commentaire.save()

                return redirect('detail_article', id=article.id)

    context = {
        'article': article,
        'commentaires': commentaires,
        'form': form
    }
    return render(request, 'article_detail.html',context)    

@login_required
def supprimer_commentaire(request, id):
    # Récuperer le commetaire à supprimer
    commentaire = get_object_or_404(Commentaire, id=id)
    
    # verifier l'auteur du commentaire
    if commentaire.user != request.user:
        return redirect('detail_article', id=commentaire.article.id)
    
    # suppression
    if request.method == "POST":
        article_id = commentaire.article.id
        commentaire.delete()
        return redirect('detail_article', id=article_id)

    # afficher la page de confirmation
    return render(request, 'supprimer_commentaire.html', {'commentaire': commentaire})


@login_required
def modifier_commentaire(request, id):
    # Récuperer le commetaire à supprimer
    commentaire = get_object_or_404(Commentaire, id=id)
    
    # verifier l'auteur du commentaire
    if commentaire.user != request.user:
        return redirect('detail_article', id=commentaire.article.id)
    
    form = CommentaireForm(instance=commentaire)
    
    # modification
    if request.method == 'POST':
        form = CommentaireForm(request.POST, instance=commentaire)
        if form.is_valid():
            form.save()
            
            return redirect('detail_article', id=commentaire.article.id)
    
    # afficher la page de modification
    return render(request, 'modifier_commentaire.html', {'form': form})

