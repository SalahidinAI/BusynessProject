from rest_framework import serializers
from .models import *


class UserProfileSerializer(serializers.ModelSerializer):
    date_registered = serializers.DateTimeField(format('%d-%m-%Y %H:%M'))

    class Meta:
        model = UserProfile
        fields = '__all__'


class GroupListSerializer(serializers.ModelSerializer):
    # group_name = serializers.DateField(format('%d-%m-%Y'))
    get_count_products = serializers.SerializerMethodField()
    get_count_available_sizes = serializers.SerializerMethodField()
    get_count_all_sizes = serializers.SerializerMethodField()
    get_group_spend = serializers.SerializerMethodField()
    get_products_income = serializers.SerializerMethodField()
    get_products_profit = serializers.SerializerMethodField()

    class Meta:
        model = Group
        fields = ['group_name', 'get_count_products', 'get_count_available_sizes', 'get_count_all_sizes',
                  'get_group_spend', 'get_products_income', 'get_products_profit'] # , 'get_quantity_products', 'created_date'

    def get_count_products(self, obj):
        return obj.get_count_products()

    def get_count_available_sizes(self, obj):
        return obj.get_count_available_sizes()

    def get_count_all_sizes(self, obj):
        return obj.get_count_all_sizes()

    def get_group_spend(self, obj):
        return obj.get_group_spend()

    def get_products_income(self, obj):
        return obj.get_products_income()

    def get_products_profit(self, obj):
        return obj.get_products_profit()


class ProductSizeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSize
        fields = ['size']


class ProductSizeDetailSerializer(serializers.ModelSerializer):
    sold_date = serializers.DateTimeField(format('%d-%m-%Y %H:%M'))
    get_profit = serializers.ModelSerializer()

    class Meta:
        model = ProductSize
        fields = ['size', 'high_price', 'get_profit', 'sold_date']

    def get_profit(self, obj):
        return obj.get_profit()


class ProductListSerializer(serializers.ModelSerializer):
    sizes = ProductSizeListSerializer(many=True, read_only=True)
    get_products_spend = serializers.ModelSerializer()
    get_products_income = serializers.ModelSerializer()
    get_products_profit = serializers.ModelSerializer()

    class Meta:
        model = Product
        fields = ['id', 'image', 'product_name', 'article', 'sizes', 'get_products_spend', 'get_products_income', 'get_products_profit'] # 'group', 'description', 'low_price', 'high_price', 'created_date',

    def get_products_spend(self, obj):
        return obj.get_products_spend()

    def get_products_income(self, obj):
        return obj.get_products_income()

    def get_products_profit(self, obj):
        return obj.get_products_profit()


class GroupDetailSerializer(serializers.ModelSerializer):
    products = ProductListSerializer(many=True, read_only=True)

    class Meta:
        model = Group
        fields = ['group_name', 'products'] # , 'get_quantity_products'


class ProductDetailSerializer(serializers.ModelSerializer):
    created_date = serializers.DateTimeField(format='%d-%m-%Y %H:%M')
    sizes = ProductSizeDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['image', 'product_name', 'article', 'description', 'low_price', 'sizes', 'created_date'] # 'high_price',
