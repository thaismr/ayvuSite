from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.http import HttpResponse
from . models import BlogPost


# Create your views here.
def index(request):
    # return HttpResponse('Blog index.')
    posts = BlogPost.objects.all()
    paginator = Paginator(posts, 1)
    page = request.GET.get('p')
    posts = paginator.get_page(page)
    return render(request, 'index.html', {
        'posts': posts
    })


def blog_post(request, post_id):
    # post = BlogPost.objects.get(id=post_id)
    post = get_object_or_404(BlogPost, id=post_id)
    return render(request, 'blog_post.html', {
        'post': post
    })
