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
    # PICK_USED = False
    # PICK_NEW = True
    PICKS = [
        ('중고 기계', '중고 기계'),
        ('신품 기계', '신품 기계'),
    ]
    # 뒤에가 선택이고 앞에가 db에 들어가는 말
    category = models.CharField(max_length=20, choices=PICKS, default = '')    
    photo = ProcessedImageField(
        blank=True,
        # processors=[Thumbnail(200, 200)],
        format='jpeg',
        options={'quality': 100},
        upload_to='%Y/%m/%d/'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)




