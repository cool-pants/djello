from django.core.exceptions import ObjectDoesNotExist
from django.core.cache import cache

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.generics import get_object_or_404
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import status
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework import viewsets

from .models import Workspace
from .serializers import WorkspaceSerializer
from .permissions import IsStaffOrOwnerOrReadOnly, IsAuthenticatedForSafe

# Create your views here.

class AuthTokenView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data = request.data, context={'request':request}) 

        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token':token.key,
            })
            
@api_view()
@authentication_classes([TokenAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def logout(request):
    try:
        token = Token.objects.get(user=request.user)
        token.delete()
    except (AttributeError, ObjectDoesNotExist):
        pass
    return Response({"success": "Successfully logged out."}, 
                        status=status.HTTP_200_OK)

class WorkspaceViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication,TokenAuthentication]
    permission_classes = [IsAuthenticatedForSafe, IsStaffOrOwnerOrReadOnly]
    queryset = Workspace.objects.all()
    serializer_class = WorkspaceSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(owner=request.user)
        return Response(status=status.HTTP_201_CREATED)
