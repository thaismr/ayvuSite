from django.core.exceptions import ImproperlyConfigured
from django.db import models


class PublishedManager(models.Manager):
    """ Custom queryset manager for filtering objects by published status """
    def get_queryset(self):
        return super().get_queryset().filter(published_status='PUBLISHED')


class PublishedAbstractBase(models.Model):
    """ Abstract base for adding custom published status manager to any model """
    objects = models.Manager()  # The default manager
    pubs = PublishedManager()  # Filtered by published objects only

    class Meta:
        abstract = True


class PublishedViewsMixin:
    """ Mixin to filter objects by published status by setting the queryset to use custom manager. """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        if self.model.pubs:
            self.queryset = self.model.pubs.all()
        else:
            raise ImproperlyConfigured(
                "%(cls)s is missing a Model with custom manager for filtering by published status. "
                % {
                    'cls': self.__class__.__name__
                }
            )
