from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .permissions import IsOwnerOrReadOnly


# from account.
from .models import Recipe
from .serializers import RecipeSerializer


@api_view(['GET', ])
@permission_classes((IsAuthenticatedOrReadOnly,))
def api_detail_recipes_view(request):

    try:
        recipe = Recipe.objects.all()
    except Recipe.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = RecipeSerializer(recipe, many=True)
    return Response(serializer.data)


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
