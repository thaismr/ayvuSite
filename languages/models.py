from django.db import models


class Language(models.Model):
    name = models.CharField(max_length=50, verbose_name='Language')
    slug = models.SlugField(unique=True)
    flag = models.ImageField(
        blank=True,
        upload_to='images/flags'
    )
    summary = models.CharField(max_length=255)
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name
