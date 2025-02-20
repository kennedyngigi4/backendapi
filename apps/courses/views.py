from django.shortcuts import render
from rest_framework import status, generics, viewsets
from rest_framework.response import Response

from apps.courses.models import *
from apps.courses.serializers import *
# Create your views here.



class HomepageView(generics.ListAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.filter(is_published=True).order_by('?')[:8]


class AllCourses(generics.ListAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.filter(is_published=True)


class CourseDetails(generics.RetrieveAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.filter(is_published=True)

