# Generated by Django 3.1.6 on 2021-02-24 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0002_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='recipes',
        ),
        migrations.AddField(
            model_name='recipe',
            name='categories',
            field=models.ManyToManyField(to='recipe.Category'),
        ),
    ]