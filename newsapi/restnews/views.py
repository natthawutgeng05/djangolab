from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import NewsPost

# Create your views here.
def get_news(request):
    new_list = NewsPost.objects.all()
    data = {'result' : list(new_list.values('news_text','author','upload_date'))}
    return JsonResponse(data)

def get_news_limit(request, no):
    new_list = NewsPost.objects.all()[:no]
    data = {'result' : list(new_list.values('news_text','author','upload_date'))}
    return JsonResponse(data)

def get_news_name(request, name):
    new_list = NewsPost.objects.all(author=name)
    data = {'result' : list(new_list.values('news_text','author','upload_date'))}
    return JsonResponse(data)