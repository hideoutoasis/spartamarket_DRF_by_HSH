from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.ProductAPIView.as_view(), name="product_list"),
    path("<int:productId>/", views.ProductDetailAPIView.as_view(), name="product_detail"),
]
