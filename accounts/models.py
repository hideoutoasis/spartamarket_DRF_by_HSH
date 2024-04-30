from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password

# 비밀번호 받을 양식 따로 만들어야 함.

class User(AbstractUser):
    
    # 비밀번호 받는 함수
    def set_password(self, raw_password):
        self.password = make_password(raw_password)
    
    username = models.CharField(default='', max_lenght=20, null=False, blank=False, unique=True)
    email = models.CharField(default='', max_lenght=100, null=False, blank=False, unique=True)
    name = models.CharField(default='', max_lenght=100, null=False, blank=False)
    nickname = models.CharField(default='', max_lenght=30, null=False, blank=False, unique=True)
    birthday = models.CharField(default='', max_lenght=30, null=False, blank=False)
    
    # User 모델 관리 코드, 계정 활성화, 사용자 활성화 상태
    is_active = models.BooleanField(default=True)    
    is_admin = models.BooleanField(default=False)
    
    # 필수입력 설정
    REQUIRED_FIELDS = ["username", "email", "name", "nickname", "birthday", "password"]