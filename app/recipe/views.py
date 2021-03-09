from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Tag, Ingredient, IngredientLine, Measurement, Recipe, GroceryList
from recipe import serializers


class BaseRecipeAttrViewSet(viewsets.ModelViewSet):
    """"Base viewset for user owned recipe attributes"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def _params_to_ints(self, qs):
        """Convert a list of string IDs to a list of integers"""
        return [int(str_id) for str_id in qs.split(',')]

    def get_queryset(self):
        """Return objects for the current authenticated user only"""
        ids = self.request.query_params.get('ids')
        queryset = self.queryset
        if ids:
            ids = self._params_to_ints(ids)
            queryset = queryset.filter(id__in=ids)

        return queryset.filter(user=self.request.user).order_by('-name')

    def perform_create(self, serializer):
        """Create a new object"""
        serializer.save(user=self.request.user)


class TagViewSet(BaseRecipeAttrViewSet):
    """Manage tags in the database"""
    queryset = Tag.objects.all()
    serializer_class = serializers.TagSerializer

class IngredientViewSet(BaseRecipeAttrViewSet):
    """Manage ingredients in the database"""
    queryset = Ingredient.objects.all()
    serializer_class = serializers.IngredientSerializer

class MeasurementViewSet(BaseRecipeAttrViewSet):
    """Manage measurements in the database"""
    queryset = Measurement.objects.all()
    serializer_class = serializers.MeasurementSerializer

class IngredientLineViewSet(BaseRecipeAttrViewSet):
    """Manage ingredients in the database"""
    queryset = IngredientLine.objects.all()
    serializer_class = serializers.IngredientLineSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        """Return objects for the current authenticated user only"""
        return self.queryset.order_by('-quantity')

    def perform_create(self, serializer):
        """Create a new object"""
        serializer.save()

class RecipeViewSet(viewsets.ModelViewSet):
    """Manage recipes in the database"""
    serializer_class = serializers.RecipeSerializer
    queryset = Recipe.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def _params_to_ints(self, qs):
        """Convert a list of string IDs to a list of integers"""
        return [int(str_id) for str_id in qs.split(',')]

    def get_queryset(self):
        """Retrive the recipes for the authenticated user"""
        tags = self.request.query_params.get('tags')
        queryset = self.queryset
        if tags:
            tag_ids = self._params_to_ints(tags)
            queryset = queryset.filter(tags__id__in=tag_ids)

        return queryset.filter(user=self.request.user).order_by('-id')

    def get_serializer_class(self):
        """Return the appropriate serializer class"""
        if self.action == 'retrieve':
            return serializers.RecipeDetailSerializer

        return self.serializer_class

    def perform_create(self, serializer):
        """Create a new object"""
        serializer.save(user=self.request.user)

class GroceryListViewSet(viewsets.ModelViewSet):
    """Manage grocery lists in the database"""
    serializer_class = serializers.GroceryListSerializer
    queryset = GroceryList.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def _params_to_ints(self, qs):
        """Convert a list of string IDs to a list of integers"""
        return [int(str_id) for str_id in qs.split(',')]

    def get_queryset(self):
        """Retrive the recipes for the authenticated user"""
        queryset = self.queryset

        return queryset.filter(user=self.request.user).order_by('-id')

    def get_serializer_class(self):
        """Return the appropriate serializer class"""
        if self.action == 'retrieve':
            return serializers.GroceryListDetailSerializer

        return self.serializer_class

    def perform_create(self, serializer):
        """Create a new object"""
        serializer.save(user=self.request.user)