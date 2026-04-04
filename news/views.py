from django.shortcuts import render


def home(request):
    return render(request, 'index.html')

def liste_artciles(request):
    return render(request, 'article_list.html')

def  detail_article(request):
    return render(request, 'article_detail.html')
