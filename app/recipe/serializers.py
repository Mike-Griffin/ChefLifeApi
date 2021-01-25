from rest_framework import serializers

from core.models import Tag, Ingredient, IngredientLine, Recipe


class TagSerializer(serializers.ModelSerializer):
    """Serializer for tag objects"""

    class Meta:
        model = Tag
        fields = ('id', 'name')
        read_only_fields = ('id',)


class IngredientSerializer(serializers.ModelSerializer):
    """Serializer for ingredient objects"""

    class Meta:
        model = Ingredient
        fields = ('id', 'name')
        read_only_fields = ('id',)

class IngredientLineSerializer(serializers.ModelSerializer):
    """Serializer for ingredient objects"""
    ingredient = serializers.PrimaryKeyRelatedField(
        queryset=Ingredient.objects.all()
    )

    class Meta:
        model = IngredientLine
        fields = ('id', 'quantity','ingredient')
        read_only_fields = ('id',)

class RecipeSerializer(serializers.ModelSerializer):
    """Serializer for recipe objects"""
    tags = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Tag.objects.all()
    )

    ingredientLines = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=IngredientLine.objects.all()
    )

    class Meta:
        model = Recipe
        fields = ('id', 'title', 'tags', 'ingredientLines')
        read_only_fields = ('id',)

class RecipeDetailSerializer(RecipeSerializer):
    """Serialize a recipe detail"""
    tags = TagSerializer(many=True, read_only=True)
    ingredientLines = IngredientLineSerializer(many=True, read_only=True)