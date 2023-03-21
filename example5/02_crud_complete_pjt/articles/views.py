from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'articles/index.html', context)


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {'article': article}
    return render(request, 'articles/detail.html', context)


# def create(request):    # GET    
#     # POST이면
#     if request.method == 'POST':
#         form = ArticleForm(request.POST)
#         # 유효성 검사
#         # valid 하면
#         if form.is_valid():
#             article = form.save()
#             return redirect('articles:detail', pk=article.pk)
#         # invalid 하면
#         context = {
#             'form' : form
#         }
#         return render(request, 'articles/create.html', context)

#     # GET이면 빈 form을 보여주고
#     elif request.method == 'GET':
#         form = ArticleForm()
#         context = {
#             'form' : form
#         }
#         return render(request, 'articles/create.html', context)

    # if request.method == 'POST':
    #     title = request.POST.get('title')
    #     content = request.POST.get('content')
    #     article = Article(title=title, content=content)
    #     article.save()
    #     return redirect('articles:detail', pk=article.pk)
    # else:
    #     return render(request, 'articles/create.html')

def create(request):    # GET    
    # POST이면
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        # 유효성 검사
        # valid 하면
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', pk=article.pk)

    # GET이면 빈 form을 보여주고
    elif request.method == 'GET':
        form = ArticleForm()

    # invalid 하면
    context = {
        'form' : form
    }
    return render(request, 'articles/create.html', context)


def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')


def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        article.title = request.POST.get('title')
        article.content = request.POST.get('content')
        article.save()
        return redirect('articles:detail', pk=article.pk)
    else:
        context = {'article': article}
        return render(request, 'articles/update.html', context)
