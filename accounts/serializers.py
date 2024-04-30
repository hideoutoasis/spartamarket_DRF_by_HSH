from rest_framework import serializers
from . models import User

class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data): # 유효성 검사
        user = User.objects.create_user(
            username= validated_data['username'],
            email = validated_data['email'],
            name = validated_data['name'],
            nickname = validated_data['nickname'],
            birthday = validated_data['birthday'],
            password = validated_data['password']
        )
        return user
    
    class Meta:
        model = User
        fields = ["username", "email", "name", "nickname", "birthday", "password"]