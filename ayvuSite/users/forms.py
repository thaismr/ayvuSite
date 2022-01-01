from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django import forms

from languages.models import Language
from .models import User, UserProfile


class UserSignUpForm(UserCreationForm):
    speaks = forms.ModelMultipleChoiceField(
        queryset=Language.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label=_("Languages spoken"),
        required=True
    )

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_premium = False
        user.save()
        profile = UserProfile.objects.create(user=user)
        profile.speaks.add(*self.cleaned_data.get('speaks'))
        return user
