from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('recipes', views.recipes, name='recipes'),
    path('recipes/delete/<int:recipe_id>', views.delete_recipe, name='delete_recipe'),
]
