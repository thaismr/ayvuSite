from django.db import models
from django.utils import timezone


# TODO: Rename to just Category
class PostCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


# TODO: Rename to just Post
class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(PostCategory, on_delete=models.DO_NOTHING)
    content = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title
