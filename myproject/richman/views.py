from django.db.models import Exists, OuterRef
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .serializers import *
from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status


class RegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CustomLoginView(TokenObtainPairView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception:
            return Response({"detail": "Неверные учетные данные"}, status=status.HTTP_401_UNAUTHORIZED)

        user = serializer.validated_data
        return Response(serializer.data, status=status.HTTP_200_OK)


class LogoutView(generics.GenericAPIView):
    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class GroupListViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.filter(products__sizes__have=True).distinct()
    serializer_class = GroupListSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['products__sizes__size',] # возможно работает не корректно (+have)
    search_fields = ['products__product_name']
    ordering_fields = ['group_name', 'created_date']

    def get_queryset(self):
        size_filter = self.request.query_params.get('products__sizes__size')
        queryset = Group.objects.all()

        if size_filter:
            # Проверяем, есть ли в группе продукт с указанным размером и have=True
            queryset = queryset.filter(
                Exists(
                    ProductSize.objects.filter(
                        size=size_filter,
                        have=True,
                        product__group=OuterRef('pk')
                    )
                )
            )
        return queryset.distinct()


class GroupDetailViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all().distinct()  # Добавляем distinct()
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
