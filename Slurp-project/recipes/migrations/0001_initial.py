# Generated by Django 3.0.5 on 2020-04-28 12:13

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('slug', models.SlugField()),
                ('date_added', models.DateField(auto_now_add=True)),
                ('image', models.ImageField(null=True, upload_to='images/recipe_images')),
                ('prep_time', models.DurationField()),
                ('method', models.TextField()),
                ('submitter', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('quantity', models.PositiveIntegerField()),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=4)),
                ('recipes', models.ManyToManyField(to='recipes.Recipe')),
            ],
        ),
    ]