from django import urls
from django.urls import path

from .views import (api_detail_recipe_view,
                    api_update_recipe_view,
                    api_delete_recipe_view,
                    api_create_recipe_view
                    )

app_name = 'recipe'

urlpatterns = [
    path('<id>/', api_detail_recipe_view, name='detail'),
    path('<id>/update', api_update_recipe_view, name='update'),
    path('<id>/delete', api_delete_recipe_view, name='delete'),
    path('create', api_create_recipe_view, name='create'),
]
