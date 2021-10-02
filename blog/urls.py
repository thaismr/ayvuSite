from django.urls import path, include
from .views import BlogPostList, BlogPostDetail, BlogPostCreate, BlogPostPreview, BlogPostSearch

app_name = 'blog'

urlpatterns = [
    path('', BlogPostList.as_view(), name='index'),
    path('add/', BlogPostCreate.as_view(), name='add_entry'),
    path('search/', BlogPostSearch.as_view(), name='search'),
    path('<slug>/', include([
        path('', BlogPostDetail.as_view(), name='post'),
        path('preview/', BlogPostPreview.as_view(), name='preview'),
    ])),
]
