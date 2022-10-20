from django.shortcuts import render, redirect

from .models import TelegramUser, Recipe

def index(request):
    users = TelegramUser.objects.all().order_by('-id')
    return render(request, 'dashboard/index.html', {'users': users})


def recipes(request):
    recipes = Recipe.objects.all().order_by('-id')
    return render(request, 'dashboard/recipes.html', {'recipes': recipes})


def delete_recipe(request, recipe_id):
    Recipe.objects.filter(id=recipe_id).delete()
    return redirect('recipes')
