from django.db import models
import os
import uuid

# def user_directory_path(instance, filename):
#     ext = filename.split('.')[-1]
#     filename = '{}.{}'.format(uuid.uuid4().hex[:8], ext)
#     sub_folder = 'file'
#     if ext.lower() in ["jpg", "png", "gif"]:
#         sub_folder = "upload"
#     if ext.lower() in ["pdf", "docx"]:
#         sub_folder = "document"
#     return os.path.join(instance.id, sub_folder, filename)

class Image(models.Model):
    photo = models.ImageField(upload_to='upload',null=True,blank=True)

    def __str__(self):
        return self.photo
