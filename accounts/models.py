from django.db import models
from blog.models import BlogPost
from django import forms


# Create your models here.
class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        exclude = ('date_created',)
