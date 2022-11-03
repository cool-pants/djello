from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer
from .models import Workspace

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username']

class WorkspaceSerializer(ModelSerializer):
    class Meta:
        model = Workspace
        fields = '__all__'
        read_only_fields = ['owner', 'created_on']
    
    def create(self, validated_data, owner=None):
        print(owner)
        if owner != None:
            validated_data['owner'] = owner
        if 'members' not in validated_data:
            validated_data['members'] = []
        if validated_data['owner'] not in validated_data['members']:
            validated_data['members'].append(validated_data['owner'])
        return super().create(validated_data)

