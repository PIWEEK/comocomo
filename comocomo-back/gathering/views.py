from django.shortcuts import render
from rest_framework import viewsets
from .models import FoodKind
from .serializers import FoodKindSerializer

class FoodKindViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows foodkinds to be viewed
    """
    queryset = FoodKind.objects.all()
    serializer_class = FoodKindSerializer
