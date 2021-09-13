from django.forms import ModelForm
from .models import BlogPost


class BlogPostForm(ModelForm):
    """ form = BlogPostForm(request.user) """
    class Meta:
        model = BlogPost
        # fields = ('title', 'category', )

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['category'].queryset = Category.objects.filter(language=user.active_language)
