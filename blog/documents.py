from django_elasticsearch_dsl import (
    Document,
    fields,
    Index,
)
from django_elasticsearch_dsl.registries import registry
from .models import Post


# post_index = Index('posts')
#
# post_index.settings(
#     number_of_shards=1,
#     number_of_replicas=0
# )

@registry.register_document
class PostDocument(Document):
    class Index:
        name = 'posts'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0
        }

    # title = fields.TextField(
    #     attr='title',
    #     fields={
    #         'suggest': fields.Completion(),
    #     }
    # )
    # pub_date = fields.Date(
    #     attr='pub_date',
    # )
    # body = fields.TextField(
    #     attr='body',
    # )
    #
    # action_title = fields.TextField(attr='get_auction_title')

    # class Meta:
    #     model = Post
    #     fields = [
    #         'id',
    #         'title',
    #         'pub_date',
    #         'body',
    #     ]

    class Django:
        model = Post
        fields = [
            'id',
            'title',
            'pub_date',
            'body',
        ]

        # Ignore auto updating of Elasticsearch when a model is saved
        # or deleted:
        # ignore_signals = True

        # Don't perform an index refresh after every update (overrides global setting):
        # auto_refresh = False

        # Paginate the django queryset used to populate the index with the specified size
        # (by default it uses the database driver's default setting)
        # queryset_pagination = 5000

