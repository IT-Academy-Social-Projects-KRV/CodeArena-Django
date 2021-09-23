from rest_framework import serializers
from .models import Task, Language, Category


class TaskListSerializer(serializers.ModelSerializer):
    """Serialize all data from Task table"""

    class Meta:
        model = Task
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'


class CreateTaskSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Task
        exclude = ['_id', 'created_at', 'updated_at', 'user_id']

    def validate_languages(self, value):
        """
        Checks for languages in the database.
        """

        language_list = Language.objects.values_list('name', flat=True)

        if value in set(language_list): # for models.CharField in DB Mongo
        # if set(value).issubset(set(language_list)):
            return value

        raise serializers.ValidationError(
            'One or more items do not exist in model Language.')

    def validate_categories(self, value):
        """
        Checks for categories in the database.
        """

        category_list = Category.objects.values_list('name', flat=True)

        if set(value).issubset(set(category_list)):
            return value

        raise serializers.ValidationError(
            'One or more items do not exist in model Category.')

    def create(self, validated_data):
        return Task.objects.create(**validated_data)

