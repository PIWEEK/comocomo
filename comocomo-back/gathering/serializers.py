from .models import *
from rest_framework import serializers


class FoodKindSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FoodKind
        fields = ('name', 'description', 'icon_path')
