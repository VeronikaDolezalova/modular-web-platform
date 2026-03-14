from django.urls import path
from . import views

app_name = 'orders'  # namespace to avoid URL name conflicts

urlpatterns = [
    path('', views.package_list, name='package_list'),
    path('success/', views.order_success, name='order_success'),  # success must be before <slug>
    path('<slug:slug>/', views.package_detail, name='package_detail'),
]