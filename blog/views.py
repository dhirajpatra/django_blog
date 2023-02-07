from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .utils import print_caller
from .models import Post
from .documents import PostDocument
from .documents import PostDocumentSerializer
from django_elasticsearch_dsl_drf.constants import (
    LOOKUP_FILTER_RANGE,
    LOOKUP_QUERY_GT,
    LOOKUP_QUERY_GTE,
    LOOKUP_QUERY_IN,
    LOOKUP_QUERY_LT,
    LOOKUP_QUERY_LTE,
    SUGGESTER_COMPLETION,
)
from django_elasticsearch_dsl_drf.filter_backends import (
    DefaultOrderingFilterBackend,
    FacetedSearchFilterBackend,
    FilteringFilterBackend,
    SearchFilterBackend,
    SuggesterFilterBackend,
)
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet


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
    return render(request, 'blog/blog_search.html', {'results': results})


class PostViewSet(DocumentViewSet):
    document = PostDocument
    serializer_class = PostDocumentSerializer
    ordering = ('id',)
    lookup_field = 'id'

    filter_backends = [
        DefaultOrderingFilterBackend,
        FacetedSearchFilterBackend,
        FilteringFilterBackend,
        SearchFilterBackend,
        SuggesterFilterBackend,
    ]

    search_fields = (
        'title',
        'body',
    )

    filter_fields = {
        'id': {
            'field': 'id',
            'lookups': [
                LOOKUP_FILTER_RANGE,
                LOOKUP_QUERY_IN,
                LOOKUP_QUERY_GT,
                LOOKUP_QUERY_GTE,
                LOOKUP_QUERY_LT,
                LOOKUP_QUERY_LTE,
            ],
        },
        'title': 'title',
    }

    suggester_fields = {
        'title_suggest': {
            'field': 'title.suggest',
            'suggesters': [
                SUGGESTER_COMPLETION,
            ],
        },
    }

