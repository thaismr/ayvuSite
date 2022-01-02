from django.contrib.auth import get_user_model, login
from django.shortcuts import redirect
from django.views.generic import CreateView
from rest_framework import viewsets, permissions

from .serializers import UserSerializer, UserProfileSerializer
from .forms import UserSignUpForm
from .models import UserProfile

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    lookup_field = 'username'


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all().order_by('-user')
    serializer_class = UserProfileSerializer


# Regular HTML template views:
# ------------------------------
class UserSignUpView(CreateView):
    model = User
    form_class = UserSignUpForm
    template_name = 'registration/signup.html'

    def get_context_data(self, **kwargs):
        kwargs['is_premium'] = False
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')
