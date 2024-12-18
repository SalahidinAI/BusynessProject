from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .serializers import *
from rest_framework import viewsets


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class GroupListViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupListSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['products__sizes__size',] # возможно работает не корректно (+have)
    search_fields = ['products__product_name']
    ordering_fields = ['group_name', 'created_date']


class GroupDetailViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupDetailSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['products__sizes__size',] # возможно работает не корректно (+have)
    search_fields = ['products__product_name']
    ordering_fields = ['group_name', 'created_date']


class ProductListViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer


class ProductDetailViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer


class ProductSizeListViewSet(viewsets.ModelViewSet):
    queryset = ProductSize.objects.all()
    serializer_class = ProductSizeListSerializer


class ProductSizeDetailViewSet(viewsets.ModelViewSet):
    queryset = ProductSize.objects.all()
    serializer_class = ProductSizeDetailSerializer
