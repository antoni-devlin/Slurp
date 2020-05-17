from django import forms
from .models import Recipe, Category, Ingredient
from django.forms import ModelChoiceField, ModelMultipleChoiceField


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ["name", "image", "method", "ingredients", "category"]
        exclude = ["date_added", "prep_time"]
        labels = {
            "name": "Name",
            "image": "Image",
            "prep_time": "Preparation Time",
            "method": "Method",
            "ingredients": "Ingredients",
        }


# class RecipeForm(forms.Form):
#     name = forms.CharField(max_length=150, label='Name')
#     # image = forms.ImageField(null=True, upload_to="images")
#     prep_time = forms.DurationField(label='Preparation time')
#     method = forms.CharField(widget=forms.Textarea, label='Method')
#     ingredients = forms.ModelMultipleChoiceField(queryset=Ingredient.objects.all(), label="Ingredients")
#     category = ModelChoiceField(queryset=Category.objects.all(), label='Category')
