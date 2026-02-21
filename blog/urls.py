from django.urls import path
from . import views

app_name = 'blog'  # namespace to avoid URL name conflicts

urlpatterns = [
    path('', views.article_list, name='article_list'),
    path('search/', views.search, name='search'),  # search must be before <slug>
    path('category/<slug:slug>/', views.category_detail, name='category_detail'),
    path('<slug:slug>/', views.article_detail, name='article_detail'),
]