from django.urls import path
from apps.competitions.managers.views import *
from rest_framework.routers import DefaultRouter

routers = DefaultRouter()
routers.register(r'badges', ManagerBadgeView, basename='badges', ),
urlpatterns = routers.urls
