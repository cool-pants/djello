from django.db import transaction
from rest_framework import serializers

from .models import Story, StoryBoard, TaggedItem

from tags.serializers import TagSerializer

class StorySerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)
    class Meta:
        model = Story
        fields = "__all__"
        read_only_fields = ["id", "date_created"]

    def create(self, validated_data):
        tags_data = validated_data.pop('tags')
        print(tags_data)
        with transaction.atomic():
            story = Story.objects.create(**validated_data)
            for tag_data in tags_data:
                try:
                    tag = TaggedItem.objects.get(tag=tag_data.get('tag'))
                    story.tags.add(tag, bulk=False)
                except TaggedItem.DoesNotExist:
                    story.tags.create(tag=tag_data.get('tag'))
        return story

class StoryBoardSerializer(serializers.ModelSerializer):
    stories = StorySerializer(many=True, write_only=True)
    class Meta:
        model=StoryBoard
        fields="__all__"

    def create(self, validated_data):
        stories_data = validated_data.pop('stories')
        with transaction.atomic():
            storyboard = StoryBoard.objects.create(**validated_data)
            for story_data in stories_data:
                story_data.pop('storyboard')
                Story.objects.create(storyboard=storyboard, **story_data)
        return storyboard
