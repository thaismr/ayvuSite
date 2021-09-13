from django.db import models
from languages.models import Language


class Category(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name='Category'
    )
    language = models.ForeignKey(
        Language,
        null=True,
        blank=True,
        on_delete=models.DO_NOTHING
    )
    #: Keep translations in case original is lost
    translated_from = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        related_name='translations',
        on_delete=models.DO_NOTHING,
        verbose_name='Translated from category'
    )
    parent = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        related_name='subcategories',
        on_delete=models.DO_NOTHING,
        verbose_name='Parent category'
    )
    slug = models.SlugField(
        unique=True
    )
    image = models.ImageField(
        blank=True,
        upload_to='images/categories'
    )
    summary = models.CharField(
        max_length=255
    )
    is_featured = models.BooleanField(
        default=False
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
