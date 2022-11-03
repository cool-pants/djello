import uuid
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Workspace(models.Model):
    key = models.UUIDField(editable=False, default=uuid.uuid4(), primary_key=True)
    owner=models.ForeignKey(User, on_delete=models.CASCADE, related_name="owner")
    name=models.CharField(max_length=100)
    members = models.ManyToManyField(User, related_name="members", default=[])
    created_on = models.DateTimeField(editable=False, auto_now_add=True)

    class Meta:
        constraints = [models.UniqueConstraint(
                name="unique_user_workspace",
                fields=["name", "owner"]
                )]

    def __str__(self):
        return ('{0} - {1}'.format(self.name, self.owner.username))
