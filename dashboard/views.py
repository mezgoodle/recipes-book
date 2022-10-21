from django.shortcuts import render, redirect

from .models import TelegramUser, Recipe
from .forms import RecipeForm


def index(request):
    users = TelegramUser.objects.all().order_by('-id')
    return render(request, 'dashboard/index.html', {'users': users})


def recipes(request):
    recipes = Recipe.objects.all().order_by('-id')
    return render(request, 'dashboard/recipes.html', {'recipes': recipes})


def recipe(request, recipe_id):
    try:
        recipe_obj = Recipe.objects.get(pk=recipe_id)
    except Recipe.DoesNotExist:
        return render(request, 'dashboard/error.html', {'error': 'Рецепту з таким номером не існує'})

    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe_obj)
        if form.is_valid():
            form.save()
            return redirect('single_recipe', recipe_id=recipe_id)
    
    form = RecipeForm(instance=recipe_obj)
    return render(request, 'dashboard/recipe.html', {'form': form, 'recipe': recipe_obj})
    


def create_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=True)
            return redirect('single_recipe', recipe_id=recipe.id)
    else:
        form = RecipeForm()
    return render(request, 'dashboard/create.html', {'form': form})


def delete_recipe(request, recipe_id):
    Recipe.objects.filter(id=recipe_id).delete()
    return redirect('recipes')
