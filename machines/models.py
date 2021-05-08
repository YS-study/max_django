from django.db import models
from django.conf import settings
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail

def machines_image_path(instance, filename):
    return f'user_{instance.user.pk}/{filename}'


class Machine(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    photo = ProcessedImageField(
        black=True,
        processors=[Thumbnail(200, 200)],
        format='png','jpg','jpeg',
        options={'quality': 100},
        upload_to='%Y/%m/%d/'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    pick = models.BooleanField()




