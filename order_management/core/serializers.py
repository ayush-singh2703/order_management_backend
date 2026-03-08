from rest_framework import serializers
from .models import Restaurant, Menu, Food, Bar, Order, OrderItem


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ["id", "name", "quantity", "price", "description"]


class BarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bar
        fields = ["id", "name", "category", "quantity", "price"]


class MenuSerializer(serializers.ModelSerializer):
    food_items = FoodSerializer(many=True, read_only=True)
    bar_items = BarSerializer(many=True, read_only=True)

    class Meta:
        model = Menu
        fields = ["id", "food_items", "bar_items"]


class RestaurantSerializer(serializers.ModelSerializer):
    menu = MenuSerializer(read_only=True)

    class Meta:
        model = Restaurant
        fields = ["id", "name", "address", "type", "menu"]
        
class OrderItemSerializer(serializers.ModelSerializer):
    food = FoodSerializer(read_only=True)
    bar = BarSerializer(read_only=True)
    food_id = serializers.PrimaryKeyRelatedField(
        queryset=Food.objects.all(), source="food", write_only=True, required=False
    )
    bar_id = serializers.PrimaryKeyRelatedField(
        queryset=Bar.objects.all(), source="bar", write_only=True, required=False
    )

    class Meta:
        model = OrderItem
        fields = ["id", "food", "bar", "food_id", "bar_id", "quantity"]


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    restaurant_name = serializers.CharField(source="restaurant.name", read_only=True)

    class Meta:
        model = Order
        fields = ["id", "restaurant", "restaurant_name", "status", "created_at", "updated_at", "items"]
