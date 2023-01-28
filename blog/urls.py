from django.urls import path, include
from . import views


app_name = 'blog'

urlpatterns = [
    path('', views.BlogListView.as_view(), name='blog_list'),
    path('<int:pk>/', views.BlogDetailView.as_view(), name='blog_detail'),
]
