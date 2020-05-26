from django.shortcuts import render
from django.http import HttpResponse
from .models import ArticlePost
import markdown

# 文章列表
def article_list(request):
    # return HttpResponse("Hello World!")
    # 取出all博客文章
    articles = ArticlePost.objects.all()
    # 需要传递给模板（templates）的对象
    context = {'articles': articles}
    # render函数： 载入模板，并返回centext对象
    return render(request, 'article/list.html', context)

# 文章详情
def article_detail(request, id):
    # 取出相应文章
    article = ArticlePost.objects.get(id=id)
    # 将markdown语法渲染成html样式
    article.body = markdown.markdown(article.body,
        extensions=[
            # 包含 缩写、表格等扩展
            'markdown.extensions.extra',
            # 语法高亮扩展
            'markdown.extensions.codehilite',
        ])

    # 传递给模板对象
    context = {'articles': article}
    # 载入模板，返回context对象
    return render(request, 'article/detail.html', context)