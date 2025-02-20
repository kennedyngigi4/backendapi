from django.urls import path

from apps.courses.managers.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='courses'),
router.register(r'attachments', AttachmentViewSet, basename='attachments'),
router.register(r'chapters', ChapterViewSet, basename='chapters'),
urlpatterns = router.urls

# urlpatterns += [
#     path("courses")
# ]


