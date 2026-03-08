from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Restaurant, Menu, Food, Bar, Order, OrderItem
from .serializers import (
    RestaurantSerializer, MenuSerializer,
    FoodSerializer, BarSerializer, OrderSerializer, OrderItemSerializer
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

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_queryset(self):
        # Filter by restaurant if ?restaurant_id=x passed
        restaurant_id = self.request.query_params.get("restaurant_id")
        if restaurant_id:
            return Order.objects.filter(restaurant__id=restaurant_id)
        return super().get_queryset()

    # PATCH /api/orders/{id}/update_status/
    @action(detail=True, methods=["patch"])
    def update_status(self, request, pk=None):
        order = self.get_object()
        new_status = request.data.get("status")
        valid_statuses = ["NEW", "IN_PROGRESS", "COMPLETED", "CANCELLED"]
        if new_status not in valid_statuses:
            return Response(
                {"error": f"Invalid status. Choose from {valid_statuses}"},
                status=status.HTTP_400_BAD_REQUEST
            )
        order.status = new_status
        order.save()
        return Response(OrderSerializer(order).data)


class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

    def get_queryset(self):
        order_id = self.request.query_params.get("order_id")
        if order_id:
            return OrderItem.objects.filter(order__id=order_id)
        return super().get_queryset()