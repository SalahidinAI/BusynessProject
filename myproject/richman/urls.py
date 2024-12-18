from django.urls import path
from .views import *


urlpatterns = [
    path('', GroupListViewSet.as_view({'get': 'list', 'post': 'create'}), name='group_list'),

    path('<int:pk>/', GroupDetailViewSet.as_view({'get': 'retrieve'}), name='group_detail'),

    path('user/', UserProfileViewSet.as_view({'get': 'list'}), name='user_list'),

    path('user/<int:pk>/', UserProfileViewSet.as_view({'get': 'retrieve'}), name='user_detail'),

    path('sizes/<int:pk>/', ProductDetailViewSet.as_view({'get': 'retrieve'}), name='product_detail'),
]
