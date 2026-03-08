from rest_framework import serializers
from .models import Restaurant, Menu, Food, Bar


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
