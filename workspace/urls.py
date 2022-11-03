from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import AuthTokenView, logout, WorkspaceViewSet

router = DefaultRouter()
router.register(r'workspace', WorkspaceViewSet, basename='workspace')

urlpatterns = [
    path("get-token/", AuthTokenView.as_view()),
    path("logout/", logout),
]

urlpatterns += router.urls
