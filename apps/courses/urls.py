from django.urls import path
from apps.courses.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'courses', AllCourses, basename='courses'),
urlpatterns = router.urls

urlpatterns += [
    path( '', HomepageView.as_view(), name='home', ),
    # path( 'courses', AllCourses.as_view(), name='courses', ),
    path( 'course/<str:pk>', CourseDetails.as_view(), name='course', ),
    
]

