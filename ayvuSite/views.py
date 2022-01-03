import json

from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.http import require_POST
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .users.serializers import UserSerializer


# Create your views here.
class ProfileAPIView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, format=None):
        user = request.user
        serialized_user = UserSerializer(user)
        return Response(serialized_user.data)


@ensure_csrf_cookie
def login_set_cookie(request):
    """
    `login_view` requires that a csrf cookie be set.
    `getCsrfToken` in `auth.js` uses this cookie to
    make a request to `login_view`
    """
    return JsonResponse({"details": "CSRF cookie set"})


@require_POST
def login_view(request):
    """
    This function logs in the user and returns
    an HttpOnly cookie, the `sessionid` cookie
    """
    print(request.user)
    print(request.headers)
    print(request.body)
    if request.user.is_authenticated:
        return JsonResponse({"detail": "Success"})

    data = json.loads(request.body)
    username = data.get("username")
    password = data.get("password")
    if username is None or password is None:
        return JsonResponse(
            {"errors": {"__all__": "Please enter both username and password"}},
            status=400,
        )
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return JsonResponse({"detail": "Success"})
    return JsonResponse({"detail": "Invalid credentials"}, status=400)


def home(request):
    return render(request, 'home.html')
