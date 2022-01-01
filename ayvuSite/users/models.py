from django.utils.translation import gettext_lazy as _
from django.db import models

#: custom user model
from django.contrib.auth.models import AbstractUser
from django.conf import settings

from languages.models import Language


class User(AbstractUser):
    """Allow for updatable User models without breaking foreign keys."""
    is_premium = models.BooleanField(_("Premium"), default=False)
    active_language = models.ForeignKey(Language, default=1, on_delete=models.SET(1))


class ProxyUser(User):
    """Custom user proxy model for digested admin management."""
    class Meta:
        verbose_name = _("Digested user")
        verbose_name_plural = _("Digested users")
        proxy = True


class UserProfile(models.Model):
    """
    Extra profile data for default users.
    """
    #: User pk as profile pk
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        primary_key=True,
        on_delete=models.CASCADE,
        related_name='user_profile',
    )
    bio = models.CharField(_("Bio"), max_length=30, blank=True)
    website = models.URLField(_("Website"), max_length=255, blank=True)
    birth_date = models.DateField(_("Birth date"), null=True, blank=True)
    speaks = models.ManyToManyField(Language, verbose_name=_("Languages spoken"), related_name='speakers')

    def __str__(self):
        return str(self.user)

