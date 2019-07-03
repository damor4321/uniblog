from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path

from . import views

router = DefaultRouter()
router.register(r'blogs', views.BlogViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'entries', views.EntryViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-token-auth/', obtain_auth_token),
    url(r'^accounts/', include('rest_registration.api.urls')),
]


