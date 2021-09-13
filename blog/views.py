from django.contrib import messages
from django.db.models.functions import Concat
from django.views.generic import ListView, DetailView, UpdateView
from django.db.models import Q, Value
from . models import BlogPost

from ayvuSite.mixins import PublishedViewsMixin


class BlogPostList(PublishedViewsMixin, ListView):
    model = BlogPost
    template_name = 'index.html'
    context_object_name = 'posts'
    order_by = '-date_created'


class BlogPostDetail(PublishedViewsMixin, DetailView):
    model = BlogPost
    template_name = 'blog_post.html'
    context_object_name = 'post'


class BlogPostSearch(BlogPostList):
    """ Extends BlogPostList with search query filtering """
    # TODO: search form and validation

    def get_queryset(self):
        search_query = self.request.GET.get('q', None)

        if not search_query:
            messages.add_message(self.request, messages.ERROR, "Search field can't be empty.")
            return super().get_queryset()

        return super().get_queryset().annotate(
            full_name=Concat('author__first_name', Value(' '), 'author__last_name')
        ).filter(
            Q(title__icontains=search_query) | Q(content__icontains=search_query) |
            Q(full_name__icontains=search_query) | Q(author__username__icontains=search_query)
        )
