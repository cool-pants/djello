from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter

from .views import StoryboardViewSet, StoryViewSet

router = DefaultRouter()
router.register(r'storyboard', StoryboardViewSet, basename='storyboard')
router.register(r'story', StoryViewSet, basename='story')

urlpatterns = []

urlpatterns += router.urls
