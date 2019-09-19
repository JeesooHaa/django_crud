from django.shortcuts import render, redirect, get_object_or_404
from .models import Article


# articles 의 메인 페이지, article list 를 보여 줌 
def index(request):
    # SELECT * FROM Article
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    # render 는 url 과 상관없다. 
    return render(request, 'articles/index.html', context)


def detail(request, article_pk):
    # SELECT * FROM articles WHERE pk = article_pk
    article = get_object_or_404(Article, pk=article_pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)


# GET method 로 delete 를 하면 안되는 이유
# 아무나? 
def delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'POST':
        article.delete()
    # redirect 는 url 과 상관있다.
    # 다른 app 과 name 이 중복되면?  
        return redirect('articles:index')
    else:
        return redirect('articles:detail', article.pk)


# 데이터를 전달 받아서 article 생성
# POST /articles/create/
# REST API 는 방법론 / 해당 자원에 대한 표현 URI / 행동 METHOD 
def create(request):
    # 아니라면 (POST 일 경우) 사용자 데이터 받아서 article 생성
    if request.method == 'POST':
        # POST 로 바뀌었으니 더 이상 GET 이 아니다! 
        title = request.POST.get('title')
        content = request.POST.get('content')

        article = Article()
        article.title = title
        article.content = content
        article.save()

        # 작성 후 상세페이지 바로가기 
        # : 뒤에 띄어쓰지 말것 
        return redirect('articles:index')
        # return redirect('articles:detail', article.pk )
    # 만약 GET 요청으로 들어오면 html 페이지 rendering
    else:
        return render(request, 'articles/create.html')


def edit(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')

        article.title = title
        article.content = content
        article.save()

        return redirect('articles:detail', article.pk)
    else:
        context = {
            'article': article,
        }
        return render(request, 'articles/edit.html', context)
