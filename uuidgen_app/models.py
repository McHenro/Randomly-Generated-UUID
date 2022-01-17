from django.db import models
import uuid

class Task(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=False)

    class Meta:
        ordering = ('-created_at',)
