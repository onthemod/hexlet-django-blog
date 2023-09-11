from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
def index(request):
    context = {'app_name': 'Блог имени Хекслета'}
    return render(request, 'articles/index.html', context) 

