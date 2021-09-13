from django.db import models
from django.utils import timezone
from django.conf import settings
from categories.models import Category
from languages.models import Language

from ayvuSite.mixins import PublishedAbstractBase


class BlogPost(PublishedAbstractBase):
    title = models.CharField(
        max_length=120
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
    )
    #: Keep translations in case original is lost
    translated_from = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    language = models.ForeignKey(
        Language,
        null=True,
        blank=False,
        default=1,
        on_delete=models.SET_NULL
    )
    category = models.ForeignKey(
        Category,
        null=True,
        blank=False,
        on_delete=models.SET_NULL
    )
    slug = models.SlugField(
        unique=True,
        default='slug'
    )
    summary = models.CharField(
        max_length=255,
        null=True
    )
    featured_image = models.ImageField(
        null=True,
        blank=True,
        upload_to='images/posts/%Y/%m'
    )
    image_caption = models.CharField(
        max_length=120,
        blank=True,
        null=True
    )
    #: Only site staff or site event (e.g. community voting rules) should be able to edit
    is_featured = models.BooleanField(
        default=False
    )
    # TODO: Change to enum class with localization
    published_status = models.CharField(
        default='DRAFT',
        max_length=10,
        choices=(
            ('DRAFT', 'Draft'),  # Draft by author choice
            ('PUBLISHED', 'Published'),  # Fully visible on site
            ('PENDING', 'Pending Review'),  # Pending moderation/approval
            ('UNAPPROVED', 'Unapproved'),  # Rejected by moderation
            ('FLAGGED', 'Flagged'),  # Flagged by community
            ('DELETED', 'Deleted'),  # Mark as deleted
            ('SCHEDULED', 'Scheduled'),  # Schedule for submission
        )
    )
    date_scheduled = models.DateTimeField(
        null=True,
        blank=True,
        default=None,
        verbose_name='Schedule to publish on'
    )
    date_created = models.DateTimeField(
        default=timezone.now,
        verbose_name='Created on'
    )
    date_updated = models.DateTimeField(
        default=timezone.now,
        verbose_name='Last updated'
    )
    content = models.TextField(
        verbose_name='Post content'
    )

    class Meta:
        ordering = ('date_created', 'date_updated')

    def __str__(self):
        return self.title

