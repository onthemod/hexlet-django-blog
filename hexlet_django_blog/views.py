from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.urls import reverse

class IndexView(TemplateView):
    template_name = 'index.html'
    
    def get(self, request, *args, **kwargs):
        url = reverse('article', kwargs={'article_id': 42, 'tags': 'python'})
        return redirect(url)

    #def get_context_data(self, **kwargs):
    #   url = reverse('article', kwargs={'article_id': 42, 'tags': 'python'})
    #   return redirect(url)
		
def about(request):
    return render(request, 'about.html')


