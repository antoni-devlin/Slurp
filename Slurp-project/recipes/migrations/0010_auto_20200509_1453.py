# Generated by Django 3.0.5 on 2020-05-09 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0009_remove_recipe_submitter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='prep_time',
            field=models.TimeField(),
        ),
    ]