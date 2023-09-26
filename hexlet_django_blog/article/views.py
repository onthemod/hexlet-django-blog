from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.http import HttpResponse
from hexlet_django_blog.article.models import Article
from .forms import ArticleForm


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

class ArticleFormCreateView(View):

    def get(self, request, *args, **kwargs):
        form = ArticleForm()
        return render(request, 'articles/create.html', {'form': form})
        
    def post(self, request, *args, **kwargs):
        form = ArticleForm(request.POST)
        valid = False
        valid = form.is_valid()
        if valid:
            form.save()
            return redirect('articles') # Редирект на указанный маршрут
        # Если данные некорректные, то возвращаем человека обратно на страницу с заполненной формой
        print(f'хуууууууууууй {form.errors}')
        return render(request, 'articles/create.html', {'form': form})
