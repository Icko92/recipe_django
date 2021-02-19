from django.contrib import admin
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path('admin/', admin.site.urls),


    # REST
    path('api/recipe/', include('recipe.urls', 'recpie_api')),
    path('api/account/', include('account.urls', 'account_api')),

]
