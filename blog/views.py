from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.db.models.functions import Concat
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView
from django.db.models import Q, Value
from rest_framework import viewsets

from . models import BlogPost
from . forms import BlogPostForm

from ayvuSite.mixins import PublishedViewsMixin
from .serializers import BlogPostSerializer


class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all().order_by('-date_updated', '-date_created')
    serializer_class = BlogPostSerializer
    lookup_field = 'slug'


# Regular HTML template views:
# ------------------------------
class BlogPostList(PublishedViewsMixin, ListView):
    model = BlogPost
    template_name = 'index.html'
    context_object_name = 'posts'
    order_by = '-date_created'

    def get_queryset(self):
        return super().get_queryset().select_related('author', 'category', 'language')


class BlogPostBySelf(BlogPostList):
    """ Extends BlogPostList filtering by User's own entries """
    pass


class BlogPostDetail(PublishedViewsMixin, DetailView):
    model = BlogPost
    template_name = 'blog_post.html'
    context_object_name = 'post'

    def get_queryset(self):
        return super().get_queryset().select_related('author', 'category', 'language')


class BlogPostPreview(LoginRequiredMixin, DetailView):
    model = BlogPost
    template_name = 'blog_post.html'
    context_object_name = 'post'

    def get_queryset(self):
        """Only the author can preview post"""
        return super().get_queryset().select_related('author', 'category', 'language').filter(
            author=self.request.user
        )


class BlogPostSearch(BlogPostList):
    """ Extends BlogPostList with search query filtering """

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


class BlogPostCreate(LoginRequiredMixin, CreateView):
    model = BlogPost
    form_class = BlogPostForm

    def get_success_url(self):
        return reverse('blog:preview', kwargs={'slug': self.object.slug})

    def get_form_kwargs(self):
        """Add current user to form kwargs."""
        kwargs = super().get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

    def form_valid(self, form):
        """
        If the form is valid, updates form with request user data.
        https://docs.djangoproject.com/en/3.2/topics/class-based-views/generic-editing/#models-and-request-user
        """
        form.instance.author = self.request.user
        form.instance.language = self.request.user.active_language
        return super().form_valid(form)
