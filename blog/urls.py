from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='blog'),
    path('search/', views.search, name='search'),
    path('<int:post_id>', views.blog_post, name='blog_post'),
]
