from django.shortcuts import render, get_object_or_404
from .models import Recipe

def home(request):
    recipes = Recipe.objects
    return render(request, "recipes/home.html", {'recipes':recipes})

def recipe_detail(request, recipe_id):
    recipe_detail = get_object_or_404(Recipe, pk=recipe_id)
    return render(request, "recipes/recipe_detail.html", {'recipe':recipe_detail})
