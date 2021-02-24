from django.db.models import fields
from rest_framework import serializers
from .models import Category, Recipe


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]


class RecipeSerializer(serializers.ModelSerializer):

    categories = CategorySerializer(read_only=True, many=True)

    class Meta:
        model = Recipe
        fields = ['id', 'owner', 'title',
                  'content', 'categories', 'created_at']
