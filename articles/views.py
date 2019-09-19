from django.shortcuts import render, redirect
from .models import Article


# articles 의 메인 페이지, article list 를 보여 줌 
def index(request):
    # SELECT * FROM Article
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


def detail(request, article_pk):
    # SELECT * FROM articles WHERE pk = article_pk
    article = Article.objects.get(pk=article_pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)


def delete(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    article.delete()
    return redirect('/articles/')


# 입력 페이지 제공 
def new(request):
    return render(request, 'articles/new.html')


# 데이터를 전달 받아서 article 생성
def create(request):
    # /articles/new/ 의 new.html 의 form 에서 전달받은 데이터들 
    title = request.GET.get('title')
    content = request.GET.get('content')

    article = Article()
    article.title = title
    article.content = content
    article.save()

    # 작성 후 상세페이지 바로가기 
    return redirect(f'/articles/{article.pk}/')
