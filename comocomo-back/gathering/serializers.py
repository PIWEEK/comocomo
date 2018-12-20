from .models import *
from rest_framework import serializers


class FoodKindSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodKind
        fields = ('id', 'name', 'description', 'icon_path')


class FoodTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodType
        fields = ('id', 'kind', 'name', 'nutriscore')
