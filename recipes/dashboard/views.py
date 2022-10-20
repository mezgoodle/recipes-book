from django.shortcuts import render, redirect

from .models import TelegramUser, Recipe
from .forms import RecipeForm

def index(request):
    users = TelegramUser.objects.all().order_by('-id')
    return render(request, 'dashboard/index.html', {'users': users})


def recipes(request):
    recipes = Recipe.objects.all().order_by('-id')
    return render(request, 'dashboard/recipes.html', {'recipes': recipes})


def create_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=True)
            return
    else:
        form = RecipeForm()
    return render(request, 'dashboard/create.html', {'form': form})


def delete_recipe(request, recipe_id):
    Recipe.objects.filter(id=recipe_id).delete()
    return redirect('recipes')
