from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    image = models.ImageField(upload_to = "images/", blank=True)
    
    def __str__(self):
        return self.title