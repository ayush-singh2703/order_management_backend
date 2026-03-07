from django.shortcuts import render, get_object_or_404
from .models import Restaurant, Menu

def restaurant_list(request):
    restaurants = Restaurant.objects.all()
    return render(request, "core/restaurant_list.html", {"restaurants": restaurants})

def restaurant_detail(request, pk):
    restaurant = get_object_or_404(Restaurant, pk=pk)
    return render(request, "core/restaurant_detail.html", {"restaurant": restaurant})

def restaurant_menu(request, pk):
    restaurant = get_object_or_404(Restaurant, pk=pk)
    menu = get_object_or_404(Menu, restaurant=restaurant)
    food_items = menu.food_items.all()
    bar_items = menu.bar_items.all()
    return render(request, "core/menu.html", {
        "restaurant": restaurant,
        "food_items": food_items,
        "bar_items": bar_items,
    })
