from django.urls import path
from . import views

app_name = 'files'  # namespace to avoid URL name conflicts

urlpatterns = [
    path('', views.file_list, name='file_list'),
    path('<slug:slug>/', views.file_detail, name='file_detail'),  # optional detail page
]