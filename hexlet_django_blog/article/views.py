from django.shortcuts import render
from django.views import View

# Create your views here.
class ArticleIndexView(View):
    
    def get(self, request, *args, **kwargs):
       context = {'app_name': 'Блог имени Хекслета'}
       return render(request, 'articles/index.html', context) 

