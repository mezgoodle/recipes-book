from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('recipes', views.recipes, name='recipes'),
    path('recipes/create', views.create_recipe, name='create_recipe'),
    path('recipes/delete/<int:recipe_id>', views.delete_recipe, name='delete_recipe'),
]
