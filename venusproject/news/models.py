from django.db import models

# Create your models here.
class News(models.Model):
    image = models.ImageField(upload_to='covers/', blank=True)
    title = models.CharField(max_length=200)
    link = models.CharField(max_length=500)

    class Meta:
        ordering = ('pk',)
        verbose_name = 'news'
        verbose_name_plural = 'news'
