from django.db import models

# Create your models here.

class Gallery(models.Model):
    description = models.CharField(default="作品简介", max_length=50)
    image = models.ImageField(default='default.png', upload_to="image/")
    title = models.CharField(default='作品标题', max_length=50)

    def __str__(self):
    	return self.title
