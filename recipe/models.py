from django.db import models
from django.conf import settings


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField(blank=False, unique=True)
    image = models.ImageField(default='default.jpg', upload_to='recipe_pics')
    categories = models.ManyToManyField(Category)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
