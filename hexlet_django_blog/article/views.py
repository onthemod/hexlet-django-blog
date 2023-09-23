from django.shortcuts import render, get_object_or_404
from django.views import View
from django.http import HttpResponse
from hexlet_django_blog.article.models import Article


def index(request, tags, article_id):
    return HttpResponse(f'Статья номер {article_id}. Тег {tags}') 
    #context = {'app_name': 'Блог имени Хекслета'}
    #return render(request, 'articles/index.html', context) 

# Create your views here.
class IndexView(View):
    
    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:15]
        return render(request, 'articles/index.html', context={
            'articles': articles,
        })

class ArticleView(View):

    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs['id'])
        return render(request, 'articles/show.html', context={
            'article': article,
        })