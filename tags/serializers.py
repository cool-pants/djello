from rest_framework import serializers

from .models import TaggedItem

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaggedItem
        fields = ["tag"]

