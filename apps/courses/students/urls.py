from django.urls import path
from apps.courses.students.views import *


urlpatterns = [
    path( 'purchased_courses/', PurchasedCourses.as_view(), name='purchased_courses', ),
    path( 'purchased_course_details/<str:pk>', PurchasedCourseDetails.as_view(), name='purchased_course_details', ),
    path( 'course_details/<str:pk>', CourseDetails.as_view(), name="course_details", ),
    path( 'chapter_details/<str:pk>', ChapterDetailsView.as_view(), name='chapter_details', ),
    path( 'progress_update/<str:pk>', ProgressUpdateView.as_view(), name='progress_update', ),
    path( 'course_completion/<str:pk>', CourseCompletionView.as_view(), name='course_completion', ),
]

