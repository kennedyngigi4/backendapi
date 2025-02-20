from django.urls import path
from apps.accounts.managers.views import *
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'instructors', ManagerViewInstructors, basename='instructors'),
router.register(r'students', ManagerViewStudents, basename='students'),
urlpatterns = router.urls
