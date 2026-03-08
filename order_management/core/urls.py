from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r"restaurants", views.RestaurantViewSet)
router.register(r"menus", views.MenuViewSet)
router.register(r"food", views.FoodViewSet)
router.register(r"bar", views.BarViewSet)
router.register(r"orders", views.OrderViewSet)
router.register(r"order-items", views.OrderItemViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
]
