from django.db import models

# Create your models here.
class Involve(models.Model):
    image = models.ImageField(upload_to='covers/', blank=True)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    text = models.TextField()

    class Meta:
        ordering = ('title',)
        verbose_name = 'involved'
        verbose_name_plural = 'involved'

