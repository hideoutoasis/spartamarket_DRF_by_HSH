from django.shortcuts import render
# from django.http import JsonResponse, HttpResponse
# from django.core import serializers
from django.shortcuts import get_object_or_404
# from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .serializers import ProductSerializer

from .models import Product

class ProductAPIView(APIView):
    def get(self, request): # 상품 목록조회
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    
    # permission_classes = [ IsAuthenticated ]
    
    def post(self, request): # 상품 등록
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class ProductDetailAPIView(APIView):
    
    # permission_classes = [ IsAuthenticated ] 일단 계정 기능 만들기 전까지는 주석처리
    
    def get_object(self, productId):
        return get_object_or_404(Product, pk=productId)
    
    def get(self, request, productId): # 상세페이지 조회
        product = self.get_object(productId) 
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    
    def put(self, request, productId): # 상품 수정
        product = self.get_object(productId)
        serializer = ProductSerializer(product, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        
    def delete(self, request, productId): # 상품 삭제
        product = self.get_object(productId)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)