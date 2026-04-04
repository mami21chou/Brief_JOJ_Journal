from django.shortcuts import render

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

def liste_artciles(request):
    return render(request, 'article_list.html')

def  detail_article(request):
    return render(request, 'article_detail.html')    

