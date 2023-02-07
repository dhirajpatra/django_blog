from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .utils import print_caller
from .models import Post
from .documents import PostDocument


def home_view(request):
    print_caller()
    # to test the elasticsearch auto update index
    post = Post(
        title="First Blog Post",
        pub_date="2023-02-07 00:00:00",
        body="A beautiful car"
    )
    post.save()
    return render(request, 'blog/home.html', {'results': 'Blog post saved'})
# def blog_list(request):
#     blogs = Blog.objects.all().order_by('-pub_date')
#     return render(request, 'blog_list.html', {'blogs': blogs})


# def blog_detail(request, pk):
#     blog = Blog.objects.get(pk=pk)
#     return render(request, 'blog_detail.html', {'blog': blog})

class BlogListView(ListView):
    print_caller()
    model = Post
    template_name = 'blog/blog_list.html'
    context_object_name = 'posts'


class BlogDetailView(DetailView):
    print_caller()
    model = Post
    template_name = 'blog/blog_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        model_fields = [field.name for field in self.model._meta.get_fields()]
        context['model_fields'] = model_fields
        return context


def search_view(request):
    print_caller()
    results = PostDocument.search().query("match", title="First Blog Post")
    return render(request, 'blog/blog_list.html', {'results': results})

