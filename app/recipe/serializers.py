from rest_framework import serializers

from core.models import Tag, Ingredient, IngredientLine, Measurement, Recipe, GroceryList


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

class MeasurementSerializer(serializers.ModelSerializer):
    """Serializer for measurement objects"""

    class Meta:
        model = Measurement
        fields = ('id', 'name')
        read_only_fields = ('id',)

class IngredientLineSerializer(serializers.ModelSerializer):
    """Serializer for ingredient objects"""
    ingredient = serializers.PrimaryKeyRelatedField(
        queryset=Ingredient.objects.all()
    )
    measurement = serializers.PrimaryKeyRelatedField(
        queryset=Measurement.objects.all()
    )

    class Meta:
        model = IngredientLine
        fields = ('quantity','ingredient', 'measurement', 'order')

class RecipeSerializer(serializers.ModelSerializer):
    """Serializer for recipe objects"""
    # tags = serializers.PrimaryKeyRelatedField(
    #     many=True,
    #     queryset=Tag.objects.all()
    # )

    # tags = TagSerializer(many=True)

    ingredientLines = IngredientLineSerializer(many=True)

    class Meta:
        model = Recipe
        fields = ('id', 'title', 'tags', 'ingredientLines')
        read_only_fields = ('id',)
    
    def create(self, validated_data):
        ingredientLines_data = validated_data.pop('ingredientLines')
        tags = validated_data.pop('tags')
        recipe = Recipe.objects.create(**validated_data)
        recipe.tags.set(tags)
        for ingredientLine_data in ingredientLines_data:
            IngredientLine.objects.create(recipe=recipe, **ingredientLine_data)
        return recipe

class RecipeDetailSerializer(RecipeSerializer):
    """Serialize a recipe detail"""
    tags = TagSerializer(many=True, read_only=True)
    ingredientLines = IngredientLineSerializer(many=True, read_only=True)

class GroceryListSerializer(serializers.ModelSerializer):
    """Serializer for grocery list objects"""

    ingredientLines = IngredientLineSerializer(many=True)

    class Meta:
        model = GroceryList
        fields = ('ingredientLines', 'recipes')
        read_only_fields = ('id',)
    
    def create(self, validated_data):
        ingredientLines_data = validated_data.pop('ingredientLines')
        recipes = validated_data.pop('recipes')
        groceryList = GroceryList.objects.create(**validated_data)
        groceryList.recipes.set(recipes)
        for ingredientLine_data in ingredientLines_data:
            IngredientLine.objects.create(groceryList=groceryList, **ingredientLine_data)
        return groceryList

class GroceryListDetailSerializer(RecipeSerializer):
    """Serialize a grocery list detail"""
    recipes = RecipeSerializer(many=True, read_only=True)
    ingredientLines = IngredientLineSerializer(many=True, read_only=True)