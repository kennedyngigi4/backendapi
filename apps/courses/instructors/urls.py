from django.urls import path
from apps.courses.instructors.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='courses', ),
router.register(r'chapters', ChapterViewSet, basename='chapters', ),
urlpatterns = router.urls

urlpatterns += [
    path('assigned_courses', AssignedCourses.as_view(), name='assigned_courses', ),
    path('enrolled_students', InstructorStudentsView.as_view(), name='enrolled_students', ),
    path('student_details', InstructorStudentCourseView.as_view(), name="student_details", ),
]



