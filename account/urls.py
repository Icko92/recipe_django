from django.urls import path
from .views import CustomObtainAuthToken


from .views import (
    registration_view,
    api_detail_user_view
)


app_name = 'account'

urlpatterns = [
    path('register', registration_view, name='register'),
    path('login', CustomObtainAuthToken.as_view(), name='login'),
    path('<id>', api_detail_user_view, name='account'),
]
