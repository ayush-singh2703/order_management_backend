from django.db import models

class Restaurant(models.Model):
    class Type(models.TextChoices):
        PUB = "PUB", "pub"
        CAFE = "CAFE", "cafe"
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    type=models.CharField(max_length=10,
    choices=Type.choices)
    
    #one restr will have one menu
    
    def __str__(self):
        return self.name

class Menu(models.Model):
    restaurant = models.OneToOneField(Restaurant,
        on_delete=models.CASCADE,
        related_name="menu",
    )
    def __str__(self):
        return f"Menu for {self.restaurant.name}"
        
class Food(models.Model):
    menu = models.ForeignKey(Menu, on_delete=
    models.CASCADE, related_name="food_items")
    name=models.CharField(max_length=100)
    quantity=models.IntegerField()
    price=models.IntegerField()
    description=models.TextField(blank=True)
    
    def __str__(self):
        return self.name
        
class Bar(models.Model):
    class Category(models.TextChoices):
        BEER = "BEER", "Beer"
        WHISKEY = "WHISKEY", "Whiskey"
        RUM = "RUM", "Rum"
        VODKA = "VODKA", "Vodka"
        TEQUILA = "TEQUILA", "Tequila"
        SOFT_DRINKS = "SOFT_DRINKS", "Soft drinks"
        
    menu=models.ForeignKey(Menu,on_delete=models.CASCADE,
    related_name="bar_items")
    category=models.CharField(max_length=20,
    choices=Category.choices)
    name=models.CharField(max_length=100)
    quantity=models.IntegerField()
    price=models.IntegerField()
    
    def __str__(self):
        return f"{self.name} ({self.category})"
    
