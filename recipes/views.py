from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import Recipe
from .forms import RecipeForm


def home(request):
    recipes = Recipe.objects
    page_title = "Home"
    return render(
        request, "recipes/home.html", {"recipes": recipes, "page_title": page_title}
    )


def recipe_detail(request, recipe_id):
    recipe_detail = get_object_or_404(Recipe, pk=recipe_id)
    return render(request, "recipes/recipe_detail.html", {"recipe": recipe_detail})


def new_recipe(request):
    if request.method == "POST":
        filled_form = RecipeForm(request.POST, request.FILES)
        if filled_form.is_valid():
            created_recipe = filled_form.save()
            created_recipe_id = created_recipe.id
            message = "New recipe (%s) created successfully!" % (
                filled_form.cleaned_data["name"]
            )
            filled_form = RecipeForm()
        else:
            message = "Update failed. Pelase try again."
            created_recipe_id = None
        return render(
            request,
            "recipes/new_recipe.html",
            {
                "created_recipe_id": created_recipe_id,
                "recipeform": filled_form,
                "message": message,
            },
        )
    else:
        form = RecipeForm()
        return render(request, "recipes/new_recipe.html", {"recipeform": form})


def edit_recipe(request, recipe_id):
    recipe = Recipe.objects.get(pk=recipe_id)
    form = RecipeForm(instance=recipe)
    if request.method == "POST":
        filled_form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if filled_form.is_valid():
            filled_form.save()
            form = filled_form
    return render(
        request, "recipes/edit_recipe.html", {"recipeform": form, "recipe": recipe}
    )


def category_listing(request, category):
    recipes = Recipe.objects.filter(category__name=category)
    print(len(recipes))
    return render(request, "recipes/category_listing.html", {"recipes": recipes})
