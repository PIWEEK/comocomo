from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from django.contrib.auth.models import User
from rest_framework import viewsets
from .models import FoodKind, FoodType, FoodRegistration
from .serializers import FoodKindSerializer, FoodTypeSerializer

import json


class FoodKindViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows foodkinds to be viewed
    """
    queryset = FoodKind.objects.all()
    serializer_class = FoodKindSerializer


class FoodTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows foodkinds to be viewed
    """
    serializer_class = FoodTypeSerializer

    def get_queryset(self):
        kind_id = self.kwargs['kind_id']
        return FoodType.objects.filter(kind_id=kind_id)


class FoodRegistrationView(View):
    """
    API endpoint that allows foodregistrations to be viewed and created
    """

    def get(self, request, *args, **kwargs):
        # registrations = FoodRegistration.objects.filter(user=request.user)
        registrations = FoodRegistration.objects.all()
        from_date = request.GET.get('from')
        to_date = request.GET.get('to')
        slot = request.GET.get('slot')
        if from_date:
            registrations = registrations.filter(date__gte=from_date)
        if to_date:
            registrations = registrations.filter(date__lte=to_date)
        if slot:
            registrations = registrations.filter(slot=slot)
        return JsonResponse([registration.to_dict() for registration in registrations], safe=False)

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        # user = request.user
        user = User.objects.get(username='admin')

        FoodRegistration.objects.filter(
            user=user, date=data['date'], slot=data['slot']
        ).delete()

        if len(data['eaten']) > 0:
            registration = FoodRegistration.objects.create(
                user = user,
                date = data['date'],
                slot = data['slot'],
            )
            for food_type_data in data['eaten']:
                food_type = FoodType.objects.get(id=food_type_data['id'])
                registration.eaten.add(food_type)

        return JsonResponse({})
