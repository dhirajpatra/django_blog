# from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Post


# def blog_list(request):
#     blogs = Blog.objects.all().order_by('-pub_date')
#     return render(request, 'blog_list.html', {'blogs': blogs})


# def blog_detail(request, pk):
#     blog = Blog.objects.get(pk=pk)
#     return render(request, 'blog_detail.html', {'blog': blog})

class BlogListView(ListView):
    model = Post
    template_name = 'blog/blog_list.html'
    context_object_name = 'posts'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog/blog_detail.html'
    context_object_name = 'posts'
