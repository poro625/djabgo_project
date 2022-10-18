from django.shortcuts import render, redirect
from django.http import HttpResponse
from community.models import Article

# Create your views here.
def index(request):
    articles = Article.objects.all().order_by('-created_at') # 쿼리셋을 보여주는것이며, models.py에서 끌고 오는것이다
    context = {
        'articles':articles
    }

    return render(request, 'index.html', context)

def creative_article(request):
    if request.method == "GET":
        return render(request, 'creative_article.html')
    elif request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        Article.objects.create(title=title, content=content, user = request.user) 
        return redirect('community:index')

def article_detail(request, article_id):
    return HttpResponse('아티클 디테일')