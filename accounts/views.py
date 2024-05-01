from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSerializer
from rest_framework import generics, status

from .models import User

# 회원가입, 포스트 형식으로 받는 것 확인
class UserCreateAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
# 로그인
class LoginAPIView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        # 사용자명과 비밀번호 일치 여부를 확인
        user = authenticate(username=username, password=password)
        
        # 사용자가 존재하지 않을 경우 에러발생과 에러메세지
        if user is None:
            return Response({'message':'User information does not match'},status=status.HTTP_401_UNAUTHORIZED)
        
        # 로그인에 성공하면 토큰을 발급
        refresh = RefreshToken.for_user(user)
        return Response({'refresh_token': str(refresh), 'access_token': str(refresh.access_token), }, status=status.HTTP_200_OK)

# 프로필 조회 기능
class ProfileDetailAPIView(APIView):
    
    permission_classes = [ IsAuthenticated ]
    
    def get_object(self, username):
        return get_object_or_404(User, username=username)
    
    def get(self, request, username):
        profile = self.get_object(username)
        serializer = UserSerializer(profile)
        return Response(serializer.data)