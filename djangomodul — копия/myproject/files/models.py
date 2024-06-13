from django.db import models
from users.models import CustomUser
import os
import uuid

def upload_to(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"{uuid.uuid4()}.{ext}"
    return os.path.join('uploads/', filename)

class File(models.Model):
    file = models.FileField(upload_to=upload_to)
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(CustomUser, related_name='files', on_delete=models.CASCADE)
    shared_with = models.ManyToManyField(CustomUser, related_name='shared_files')
    file_id = models.CharField(max_length=10, unique=True)

    def save(self, *args, **kwargs):
        if not self.file_id:
            self.file_id = uuid.uuid4().hex[:10]
        super().save(*args, **kwargs)

    def rename(self, new_name):
        self.name = new_name
        self.save()
