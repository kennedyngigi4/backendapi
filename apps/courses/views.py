import django_filters
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, generics, viewsets
from rest_framework.response import Response

from apps.courses.models import *
from apps.courses.serializers import *
# Create your views here.


# FILTERS
class CourseFilter(django_filters.FilterSet):
    category = django_filters.CharFilter(field_name="category", lookup_expr="exact")

    class Meta:
        model = Course
        fields = [
            'category'
        ]

# VIEWS
class HomepageView(generics.ListAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.filter(is_published=True).order_by('?')[:8]


class AllCourses(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.filter(is_published=True)
    filter_backends = [DjangoFilterBackend]
    filterset_class = CourseFilter


class CourseDetails(generics.RetrieveAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.filter(is_published=True)

