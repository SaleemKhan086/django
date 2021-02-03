from django.db import models
from django.conf import settings
from datetime import datetime
# Create your models here.
class Task(models.Model):
    heading = models.CharField(max_length=200, null=False, blank=False)
    description = models.TextField(blank=True)
    finished = models.BooleanField(default=False)
    deadline = models.DateTimeField(default=datetime.now)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.heading
