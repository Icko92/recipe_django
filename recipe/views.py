from re import search
from rest_framework import serializers, status, views
from rest_framework import pagination
from rest_framework import response, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication
from .permissions import IsOwnerOrReadOnly
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework.filters import SearchFilter, OrderingFilter


# from account.
from .models import Recipe, Category
from .serializers import RecipeSerializer, CategorySerializer


@api_view(['GET', ])
@permission_classes((IsAuthenticated,))
def api_detail_recipe_view(request, id):

    try:
        recipe = Recipe.objects.get(id=id)
    except Recipe.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = RecipeSerializer(recipe)
    return Response(serializer.data)


@api_view(['PUT', ])
@permission_classes((IsOwnerOrReadOnly,))
def api_update_recipe_view(request, id):

    try:
        recipe = Recipe.objects.get(id=id)
    except Recipe.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    user = request.user
    if recipe.owner != user:
        return Response({'response': 'You dont have permission'})

    serializer = RecipeSerializer(recipe, data=request.data)
    data = {}
    if serializer.is_valid():
        serializer.save()
        data['success'] = 'update successful'
        return Response(data=data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE', ])
@permission_classes((IsOwnerOrReadOnly,))
def api_delete_recipe_view(request, id):

    try:
        recipe = Recipe.objects.get(id=id)
    except Recipe.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    user = request.user
    if recipe.owner != user:
        return Response({'response': 'You dont have permission'})

    operation = recipe.delete()
    data = {}
    if operation:
        data['success'] = 'delete successful'
    else:
        data['failure'] = 'delete failed'
    return Response(data=data)


@api_view(['POST', ])
@permission_classes((IsAuthenticated,))
def api_create_recipe_view(request):

    account = request.user

    recipe = Recipe(owner=account)

    serializer = RecipeSerializer(recipe, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ApiRecipeBlogView(ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)
    pagination_class = PageNumberPagination
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('title', 'content', 'categories__name', 'owner__username')


class ApiRecipeCategoryView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)
    pagination_class = None
