from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.http import HttpResponse, Http404
from django.db.models.functions import Concat
from django.db.models import Q, Value
from . models import BlogPost


# Create your views here.
def index(request):
    # return HttpResponse('Blog index.')
    # posts = BlogPost.objects.all()
    posts = BlogPost.objects.order_by('-id').filter(
        is_published=True
    )
    paginator = Paginator(posts, 1)
    page = request.GET.get('p')
    posts = paginator.get_page(page)
    return render(request, 'index.html', {
        'posts': posts
    })


def blog_post(request, post_id):
    # post = BlogPost.objects.get(id=post_id)
    post = get_object_or_404(BlogPost, id=post_id)

    if not post.is_published:
        raise Http404()

    return render(request, 'blog_post.html', {
        'post': post
    })


def search(request):
    term = request.GET.get('term')

    if term is None or not term:
        raise Http404()

    # full_name = Concat('first_name', Value(' '), 'last_name')
    #
    # posts = BlogPost.objects.annotate(
    #     relevant=full_name
    # ).filter(
    #     relevant__icontains=term,
    #     is_published=True,
    # )

    posts = BlogPost.objects.order_by('-id').filter(
        Q(title__icontains=term) | Q(content__icontains=term),
        is_published=True,
    )

    print(posts.query)
    paginator = Paginator(posts, 1)
    page = request.GET.get('p')
    posts = paginator.get_page(page)
    return render(request, 'search.html', {
        'posts': posts
    })
