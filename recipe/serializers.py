from django.db.models import fields
from rest_framework import serializers
from .models import Category, Recipe


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]


class RecipeSerializer(serializers.ModelSerializer):

    # categories = CategorySerializer(many=True)
    username = serializers.SerializerMethodField('get_username_from_owner')

    class Meta:
        model = Recipe
        fields = ['id', 'username',  'title',
                  'content', 'image', 'categories', 'created_at']
        depth = 1

    def get_username_from_owner(self, recipe):
        username = recipe.owner.username
        return username
