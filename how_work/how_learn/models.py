from django.db import models


class ModelContent(models.Model):
    name=models.CharField(max_length=23)
    content=models.CharField(max_length=345)
    zip_code = models.CharField(max_length=34)
    phone = models.CharField(max_length=23)
    # image_field = models.ImageField(null=True, blank=True, upload_to='images/')

    def __str__(self):
        return self.name
    

    
