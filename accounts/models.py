from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.db import models
from blog.models import BlogPost
from django import forms


class User(AbstractUser):
    """Allow for updatable User models without breaking foreign keys."""
    is_premium = models.BooleanField(_("Premium user?"), default=False)


class UserProfile(models.Model):
    """
    Extra profile data for default users.
    """
    user = models.OneToOneField(
        User,
        primary_key=True,
        on_delete=models.CASCADE,
        related_name='user_profile',
    )
    bio = models.CharField(_("Bio"), max_length=30, blank=True)
    website = models.URLField(_("Website"), max_length=255, blank=True)
    birth_date = models.DateField(_("Birth date"), null=True, blank=True)


# Create your models here.
class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        exclude = ('date_created',)
