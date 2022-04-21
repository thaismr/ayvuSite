from django.db import models
from simple_history.models import HistoricalRecords


class BaseModel(models.Model):
    """Model definition for BaseModel."""

    status = models.BooleanField('Status', default=True)
    created_date = models.DateField('Created at', auto_now=False, auto_now_add=True)
    modified_date = models.DateField('Modified at', auto_now=True, auto_now_add=False)
    deleted_date = models.DateField('Deleted at', auto_now=True, auto_now_add=False)
    history = HistoricalRecords(inherit=True)

    # @property
    # def _history_user(self):
    #     return self.changed_by
    #
    # @_history_user.setter
    # def _history_user(self, value):
    #     self.changed_by = value

    class Meta:
        abstract = True
