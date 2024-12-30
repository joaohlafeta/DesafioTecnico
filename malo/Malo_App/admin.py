from django.contrib import admin
from .models import Ingredient,Mesa,Dish,Category, DishIngredient, Order, Garcom, OrderDish, Invoice

# Register your models here.

admin.site.register(Ingredient)
admin.site.register(Mesa)
admin.site.register(Dish)
admin.site.register(Category)
admin.site.register(DishIngredient)
admin.site.register(Order)
admin.site.register(Garcom)
admin.site.register(OrderDish)
admin.site.register(Invoice)