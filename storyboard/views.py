from rest_framework import viewsets, permissions
from rest_framework.authentication import BasicAuthentication, TokenAuthentication

from .models import StoryBoard, Story
from .serializers import StoryBoardSerializer, StorySerializer

# Create your views here.
class StoryboardViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication, TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    queryset = StoryBoard.objects.all()
    serializer_class = StoryBoardSerializer

class StoryViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication, TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    queryset = Story.objects.all()
    serializer_class = StorySerializer
