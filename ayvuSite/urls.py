"""ayvuSite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers
from . import views

from .users.views import UserSignUpView, UserViewSet, UserProfileViewSet
from blog.views import BlogPostViewSet
from languages.views import LanguageAPIView, language_api_view, language_detail_api_view


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'profiles', UserProfileViewSet)
router.register(r'blog', BlogPostViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    # path("api/languages/", LanguageAPIView.as_view(), name="languages"),
    path("api/languages/", language_api_view, name="languages"),
    path("api/languages/<int:pk>/", language_detail_api_view, name="languages-detail"),
    path("api/login-set-cookie/", views.login_set_cookie, name="login-cookie"),
    path("api/user-data/", views.ProfileAPIView.as_view(), name="user-data"),
    path("api/login/", views.login_view, name="login-view"),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', UserSignUpView.as_view(), name='signup'),
    path('blog/', include('blog.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    #: Necessario para django-summernote
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
