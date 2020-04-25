from django.shortcuts import render

def home(request):
   return render(request, "recipes/home.html")

def recipe_detail(request, slug=slug):
    slug = "slug"
    return render(request, "recipes/recipe_detail.html", {'slug':slug})
