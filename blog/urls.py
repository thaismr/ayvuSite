from django.urls import path, include
from .views import BlogPostList, BlogPostDetail, BlogPostSearch

app_name = 'blog'

urlpatterns = [
    path('', BlogPostList.as_view(), name='index'),
    path('search/', BlogPostSearch.as_view(), name='search'),
    path('<slug>', BlogPostDetail.as_view(), name='post'),
    # path('<slug>/', include([
    #     path('history/', history),
    #     path('edit/', edit),
    #     path('discuss/', discuss),
    # ])),
]
