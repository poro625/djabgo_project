from django.shortcuts import render, redirect
from django.http import HttpResponse
from community.models import Article
from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):
    articles = Article.objects.all().order_by('-created_at') # 쿼리셋을 보여주는것이며, models.py에서 끌고 오는것이다 DB에 있는 article 다 가지고와 라는 뜻임
    context = {
        'articles':articles
    }

    return render(request, 'index.html', context)

def creative_article(request):
    if request.method == "GET":                              # GET만 하고 POST를 안할시 didn't return an Http~~~ 어쩌구 에러가 뜬다
        return render(request, 'creative_article.html')
    elif request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        Article.objects.create(title=title, content=content, user = request.user) 
        return redirect('community:index')

def article_detail(request, article_id):
    article = get_object_or_404(Article, id = article_id)    
    context = {
        'article' : article

    }
    return render(request, 'article_detail.html', context)