from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination # 페이지네이션
from rest_framework import status
from .serializers import ProductSerializer

from .models import Product

# 전역으로 정의해둔 페이지네이션을 상속하고 커스텀
class CustomPagination(PageNumberPagination):
    page_size = 10

class ProductAPIView(APIView):
    # 이 클래스 안에서 부분적으로 접근제한을 할 수 있게 위로 함수를 뻬고 아래에서 오버라이딩
    def get_permissions(self):
        if self.request.method == 'POST':
            return [ IsAuthenticated() ]
        return []
    
    def get(self, request): # 상품 목록조회 / 페이지네이션
        products = Product.objects.all().order_by("-pk")
        paginator = CustomPagination()
        result_page = paginator.paginate_queryset(products, request)
        serializer = ProductSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)
    
    def post(self, request): # 상품 등록
        serializer = ProductSerializer(data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class ProductDetailAPIView(APIView):
    
    permission_classes = [IsAuthenticated]
    
    def get_object(self, productId):
        return get_object_or_404(Product, pk=productId)
    
    def get(self, request, productId): # 상세페이지 조회
        product = self.get_object(productId)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    
    def put(self, request, productId): # 상품 수정
        product = self.get_object(productId)
        if product.author == request.user:  # 작성자인지 확인
            serializer = ProductSerializer(product, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"error": "You are not the author of this product."}, status=status.HTTP_403_FORBIDDEN)
        
    def delete(self, request, productId): # 상품 삭제
        product = self.get_object(productId)
        if product.author == request.user:# 작성자인지 확인
            product.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"error": "You are not the author of this product."}, status=status.HTTP_403_FORBIDDEN)