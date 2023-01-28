from django.core.management.base import BaseCommand
from django.utils import timezone
from blog.models import Post


class Command(BaseCommand):
    help = 'Create seed data for the Post model'

    def handle(self, *args, **kwargs):
        Post.objects.create(
            title='First Blog Post',
            body='This is the body of the first blog post.',
            pub_date=timezone.now()
        )
        Post.objects.create(
            title='Second Blog Post',
            body='This is the body of the second blog post.',
            pub_date=timezone.now()
        )
        self.stdout.write(self.style.SUCCESS('Successfully created seed data for Post model'))
