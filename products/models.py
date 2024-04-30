from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    image = models.ImageField(upload_to = "images/", blank=True)
    # 로그인 상태는 계정관련 추가한 후에 다시 마이그레이션하자
    
    def __str__(self):
        return self.title