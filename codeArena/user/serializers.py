from django.db import models
from rest_framework import serializers
from user.models import User, Coder


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password', 'placeholder': 'Password'}
    )

    class Meta:
        model = User
        fields = ['id', 'email', 'nickname', 'first_name', 'last_name',
                  'password', 'role_id', 'created_at', 'updated_at', 'status']


def create(self, validated_data):
    if "password" in validated_data:
        from django.contrib.auth.hashers import make_password
        validated_data["password"] = make_password(validated_data["password"])
    return super(UserSerializer, self).create(validated_data)


def update(self, instance, validated_data):
    if "password" in validated_data:
        from django.contrib.auth.hashers import make_password
        validated_data["password"] = make_password(validated_data["password"])
    return super(UserSerializer, self).update(instance, validated_data)


class CoderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coder
        fields = ['id', 'city', 'description', 'phone_number', 'level_id']
