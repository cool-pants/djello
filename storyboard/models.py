import uuid
from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericRelation

from workspace.models import Workspace
from tags.models import TaggedItem

# Create your models here.
class StoryBoard(models.Model):
    workspace = models.ForeignKey(Workspace, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    key=models.CharField(max_length=200, primary_key=True, editable=False, default="__")

    class Meta:
        constraints = [models.UniqueConstraint(
                name="unique name_workspace",
                fields=["workspace", "name"]
                )]

    def save(self, *args, **kwargs):
        if self.key == "__":
            self.key = (self.key).join([str(self.name), str(self.workspace)])
        super(StoryBoard, self).save(*args, **kwargs)

    def __str__(self):
        return ('{0} in {1}'.format(self.name, self.workspace))

class Story(models.Model):
    id = models.UUIDField(primary_key=True,
                          default=uuid.uuid4,
                          editable=False)
    title = models.CharField(max_length=100)
    date_created = models.DateField(auto_now_add=True, editable=False)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    storyboard = models.ForeignKey(StoryBoard, on_delete=models.CASCADE)
    tags = GenericRelation(TaggedItem)

    def __str__(self):
        return ('{0} in {1}'.format(self.title, self.storyboard.name))
