from django.contrib.auth import get_user_model
from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    image = models.ImageField(upload_to = "images/", blank=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title