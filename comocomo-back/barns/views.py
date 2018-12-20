from django.shortcuts import render
from gathering.models import FoodKind, FoodType
from django.views import View
from django.http import JsonResponse

class WeekStatisticsView(View):

    def get(self, request, **kwargs):
        from_date = kwargs['from_date']
        to_date = kwargs['to_date']

        # types = FoodType.objects.filter(foodregistration__user=request.user, foodregistration__date__range=(from_date, to_date))
        types = FoodType.objects.filter(foodregistration__date__range=(from_date, to_date))

        return JsonResponse([type.to_dict() for type in types], safe=False)
