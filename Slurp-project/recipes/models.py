from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class Ingredient(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class Recipe(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False)
    date_added = models.DateField(auto_now_add=True, editable=False)
    image = models.ImageField(null=True, upload_to="images")
    prep_time = models.TimeField(null=True)
    method = RichTextField()
    ingredients = models.ManyToManyField(Ingredient)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name
