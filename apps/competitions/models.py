import uuid
from django.db import models

# Create your models here.


class Badge(models.Model):
    badge_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=255, null=True)
    image = models.ImageField(upload_to="badges", null=True)
    created_by = models.CharField(max_length=255, null=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def imagePath(self):
        return f"http://127.0.0.1:8000{self.image.url}"

    def __str__(self):
        return self.name


