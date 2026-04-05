from django.shortcuts import render,get_object_or_404
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
# Create your views here.


class InscriptionView(CreateView):
    form_class=UserCreationForm
    template_name='registration/inscription.html'
    success_url= reverse_lazy('login')



def home(request):
    return render(request, 'index.html')

def liste_article(request):
    articles=Article.objects.all()
    return render(request, 'article_list.html',{'articles':articles})

def  detail_article(request,id):
    details=get_object_or_404(Article,pk=id)
    return render(request, 'article_detail.html',{'details':details})    

