from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Restaurant, Menu, Food, Bar
from .serializers import (
    RestaurantSerializer, MenuSerializer,
    FoodSerializer, BarSerializer
)


class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

    # GET /restaurants/{id}/menu/
    @action(detail=True, methods=["get"])
    def menu(self, request, pk=None):
        restaurant = self.get_object()
        menu = Menu.objects.get(restaurant=restaurant)
        serializer = MenuSerializer(menu)
        return Response(serializer.data)


class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer

    def get_queryset(self):
        # Filter by menu if ?menu_id=x is passed
        menu_id = self.request.query_params.get("menu_id")
        if menu_id:
            return Food.objects.filter(menu__id=menu_id)
        return super().get_queryset()


class BarViewSet(viewsets.ModelViewSet):
    queryset = Bar.objects.all()
    serializer_class = BarSerializer

    def get_queryset(self):
        menu_id = self.request.query_params.get("menu_id")
        if menu_id:
            return BarItem.objects.filter(menu__id=menu_id)
        return super().get_queryset()
