from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

def index(request, tags, article_id):
    return HttpResponse(f'Статья номер {article_id}. Тег {tags}') 
    #context = {'app_name': 'Блог имени Хекслета'}
    #return render(request, 'articles/index.html', context) 

# Create your views here.
class ArticleIndexView(View):
    
    def get(self, request, *args, **kwargs):
       context = {'app_name': 'Блог имени Хекслета'}
       return render(request, 'articles/index.html', context) 

