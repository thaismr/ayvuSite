from django.forms import ModelForm
from categories.models import Category
from .models import BlogPost


class BlogPostForm(ModelForm):
    """ Call this as BlogPostForm(request.user, *args, **kwargs) """
    class Meta:
        model = BlogPost
        fields = ['title', 'category', 'slug', 'summary', 'content']

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].queryset = Category.objects.filter(language=user.active_language)
