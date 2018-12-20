from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from rest_framework import viewsets
from .models import FoodKind, FoodType, FoodRegistration
from .serializers import FoodKindSerializer

import json


class FoodKindViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows foodkinds to be viewed
    """
    queryset = FoodKind.objects.all()
    serializer_class = FoodKindSerializer


class FoodRegistrationView(View):
    """
    API endpoint that allows foodregistrations to be viewed and created
    """

    def get(self, request, *args, **kwargs):
        registrations = FoodRegistration.objects.filter(user=request.user)
        return JsonResponse([registration.to_dict() for registration in registrations], safe=False)

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        registration = FoodRegistration.objects.create(
            user = request.user,
            date = data['date'],
            slot = data['slot'],
        )
        for type_id in data['eaten']:
            food_type = FoodType.objects.get(id=type_id)
            registration.eaten.add(food_type)
        return JsonResponse({})

