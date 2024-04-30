from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer
from rest_framework import generics

from .models import User

# 회원가입
class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ProfileDetailAPIView(APIView):
    
    permission_classes = [ IsAuthenticated ] # 로그인한 사용자만 접근가능
    
    def get_object(self, username):
        return get_object_or_404(User, pk=username)
    
    def get(self, request, username): # 프로필 조회 기능
        profile = self.get_object(username)
        serializer = UserSerializer(profile)
        return Response(serializer.data)