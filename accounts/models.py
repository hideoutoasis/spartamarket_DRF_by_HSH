from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser

class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, name, nickname, birthday, password=None, **extra_fields):
        if not username:
            raise ValueError('must have user username')
        if not email:
            raise ValueError('must have user email')
        if not name:
            raise ValueError('must have user name')
        if not nickname:
            raise ValueError('must have user nickname')
        if not birthday:
            raise ValueError('must have user birthday')
    # 필수 입력값 미입력 시 의도적으로 에러를 발생시킴
        
        user = self.model(
            username = username,
            email=self.normalize_email(email), # 중복 최소화
            name = name,
            nickname = nickname,
            birthday = birthday,
            **extra_fields
        )
        
        user.set_password(password)
        user.save()
        
        return user
    
    def create_superuser(self, username, email, password, **extra_fields):
        
        # 비밀번호 입력 안할 시 의도적으로 오류를 일으키는 방어 코드
        if password is None:
            raise TypeError('Superuser must have password')
        
        user = self.create_user(username, email, password, **extra_fields)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        
        return user


class User(AbstractUser):
    email = models.EmailField(default='', max_length=100, null=False, blank=False, unique=True)
    name = models.CharField(default='', max_length=100, null=False, blank=False)
    nickname = models.CharField(default='', max_length=100, null=False, blank=False, unique=True)
    birthday = models.DateField()
    
    # 사용자 관리 및 인증 문제를 해결하기 위한 코드
    is_active = models.BooleanField(default=True)    
    is_superuser = models.BooleanField(default=False)
    
    # 헬퍼 클래스 사용, 이 클래스를 통해 객체를 생성
    objects = CustomUserManager()
    
    # 회원가입을 위해 필수 작성해야 하는 요소들, username과 password는 AbstractUser에서 기본적으로 받기 때문에 넣으면 마이그레이션할 때 에러가 난다.
    REQUIRED_FIELDS = ["email", "name", "nickname", "birthday"]
    # first name과 last name도 기본적으로 받기 때문에 안넣어줘도 될 듯.