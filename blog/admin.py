from django.contrib import admin
from .models import Category, Article

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Admin configuration for Category model."""
    list_display = ('name',) # show the name field in the category list
    prepopulated_fields = {'slug': ('name',)} # auto-fill slug from name

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    """Admin configuration for Article model."""
    list_display = ('title', 'published', 'is_published') # show these fields in the article list
    list_filter = ('is_published', 'categories') # add filters for published status and categories
    search_fields = ('title', 'perex', 'content') # allow searching by title, perex, and content
    prepopulated_fields = {'slug': ('title',)} # auto-fill slug from title
