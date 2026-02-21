from django.shortcuts import render, get_object_or_404
from .models import Article, Category


def article_list(request):
    """Display a list of all published articles."""
    articles = Article.objects.filter(is_published=True)
    return render(request, 'blog/article_list.html', {'articles': articles})


def article_detail(request, slug):
    """Display a single article identified by slug.
    Only published articles are shown, otherwise 404 is returned.
    """
    article = get_object_or_404(Article, slug=slug, is_published=True)
    return render(request, 'blog/article_detail.html', {'article': article})


def category_detail(request, slug):
    """Display all published articles in a given category."""
    category = get_object_or_404(Category, slug=slug)
    articles = category.articles.filter(is_published=True)
    return render(request, 'blog/category_detail.html', {
        'category': category,
        'articles': articles,
    })


def search(request):
    """Search articles by title, perex or content."""
    query = request.GET.get('q', '')  # get search term from URL parameter
    articles = Article.objects.filter(
        is_published=True,
        title__icontains=query
    ) | Article.objects.filter(
        is_published=True,
        perex__icontains=query
    ) | Article.objects.filter(
        is_published=True,
        content__icontains=query
    ) if query else Article.objects.none()

    return render(request, 'blog/search.html', {
        'articles': articles,
        'query': query,
    })