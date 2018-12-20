"""comocomo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path, re_path
from rest_framework import routers
from gathering import views as gathering_views
from barns import views as barns_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('rest_auth.urls')),
    path('api/v1/food-kinds/', gathering_views.FoodKindViewSet.as_view({'get': 'list'}), name='food-kinds'),
    path('api/v1/food-kinds/<kind_id>/food-types/', gathering_views.FoodTypeViewSet.as_view({'get': 'list'}), name='food-types'),
    path('api/v1/food-registrations/', gathering_views.FoodRegistrationView.as_view(), name='food-registrations'),
    path('api/v1/week-statistics/<from_date>/<to_date>/', barns_views.WeekStatisticsView.as_view(), name='week-statistics'),
]
