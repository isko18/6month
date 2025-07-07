from django.db import models
from django.conf import settings
# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Автор"
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Заголовок"
    )
    content = models.TextField(
        verbose_name="Содержимое"
    )
    image = models.ImageField(
        upload_to='post_image/',
        null=True,
        blank=True,
        verbose_name="Фото"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания"
    )
    
    def __str__(self):
        return self.title
    
    class Meta:
        managed = False
        verbose_name = "Публикация"
        verbose_name_plural = "Публикации"
        