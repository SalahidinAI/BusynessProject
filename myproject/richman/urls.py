from django.urls import path
from .views import *


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('', GroupListViewSet.as_view({'get': 'list', 'post': 'create'}), name='group_list'),

    path('<int:pk>/', GroupDetailViewSet.as_view({'get': 'retrieve'}), name='group_detail'),

    path('user/', UserProfileViewSet.as_view({'get': 'list'}), name='user_list'),

    path('user/<int:pk>/', UserProfileViewSet.as_view({'get': 'retrieve'}), name='user_detail'),

    path('sizes/<int:pk>/', ProductDetailViewSet.as_view({'get': 'retrieve', 'put': 'update'}), name='product_detail'),
]
