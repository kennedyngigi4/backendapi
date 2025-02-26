from django.shortcuts import render, get_object_or_404

from rest_framework import generics, status, viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


from apps.courses.models import *
from apps.courses.serializers import *
from apps.courses.instructors.instructor_serializers import *


class AssignedCourses(generics.ListAPIView):
    permission_classes = [ IsAuthenticated ]
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

    def get_queryset(self):
        queryset = Course.objects.filter(instructor=self.request.user.uid).order_by("-created_at")
        return queryset


class CourseViewSet(viewsets.ViewSet):
    def create(self, request):
        try:
            if self.request.user.role == "Instructor" and self.request.user.is_verified:
                serializer = CourseSerializer(data=request.data)
                if serializer.is_valid():
                    course = serializer.save(instructor=self.request.user.uid)
                    return Response({ "course": course.course_id,  "status_code": status.HTTP_201_CREATED})
                else:
                    return Response(status.HTTP_400_BAD_REQUEST)
            else:
                return Response(status.HTTP_403_FORBIDDEN)
        except:
            return Response(status.HTTP_500_INTERNAL_SERVER_ERROR)
        

    def list(self, request):
        try:
            if self.request.user.role == "Instructor" and self.request.user.is_verified:
                queryset = Course.objects.filter(instructor=self.request.user.uid).order_by('-created_at')
                serializer = CourseSerializer(queryset, many=True)
                return Response(serializer.data)
            else:
                return Response(status.HTTP_403_FORBIDDEN)
        except:
            return Response(status.HTTP_500_INTERNAL_SERVER_ERROR)


    def retrieve(self, request, pk=None):
        try:
            if self.request.user.role == "Instructor" and self.request.user.is_verified:
                queryset = Course.objects.all()
                course = get_object_or_404(queryset, course_id=pk)
                
                if course:
                    serializer = CourseSerializer(course)
                    return Response(serializer.data)
                else:
                    return Response(status.HTTP_404_NOT_FOUND)
            else:
                return Response(status.HTTP_403_FORBIDDEN)
        except:
            return Response(status.HTTP_500_INTERNAL_SERVER_ERROR)


    def partial_update(self, request, pk=None):
        try:
            
            if self.request.user.role == "Instructor" and self.request.user.is_verified:
                print(request.data)
                course = Course.objects.get(course_id=pk)
                serializer = CourseSerializer(instance=course, data=request.data)
                if serializer.is_valid():
                    
                    serializer.save()
                    return Response(status.HTTP_200_OK)
                else:
                    return Response(status.HTTP_400_BAD_REQUEST)
            else:
                return Response(status.HTTP_403_FORBIDDEN)
        except:
            return Response(status.HTTP_500_INTERNAL_SERVER_ERROR)
    

    def destroy(self, request, pk=None):
        try:
            if self.request.user.role == "Instructor" and self.request.user.is_verified:
                queryset = Course.objects.all()
                course = get_object_or_404(queryset, course_id=pk)

                if course:
                    course.delete()
                    return Response(status.HTTP_200_OK)
                else:   
                    return Response(status.HTTP_404_NOT_FOUND)
            else:
                return Response(status.HTTP_403_FORBIDDEN)
        except:
            return Response(status.HTTP_500_INTERNAL_SERVER_ERROR)
        



class ChapterViewSet(viewsets.ViewSet):
    def create(self, request):
        try:
            if self.request.user.role == "Instructor" and self.request.user.is_verified:
                serializer = ChapterSerializer(data=request.data)
                if serializer.is_valid():
                    chapter = serializer.save(instructor=self.request.user.uid)
                    
                    return Response({ "chapter": chapter.chapter_id,  "status_code": status.HTTP_201_CREATED})
                else:
                    return Response(status.HTTP_400_BAD_REQUEST)
            else:
                return Response(status.HTTP_403_FORBIDDEN)
        except:
            return Response(status.HTTP_500_INTERNAL_SERVER_ERROR)


    def list(self, request):
        try:
            if self.request.user.role == "Instructor" and self.request.user.is_verified:
                queryset = Chapter.objects.filter(instructor=self.request.user.uid).order_by('-created_at')
                serializer = ChapterSerializer(queryset, many=True)
                return Response(serializer.data)
            else:
                return Response(status.HTTP_403_FORBIDDEN)
        except:
            return Response(status.HTTP_500_INTERNAL_SERVER_ERROR)


    def retrieve(self, request, pk=None):
        try:
            if self.request.user.role == "Instructor" and self.request.user.is_verified:
                queryset = Chapter.objects.all()
                chapter = get_object_or_404(queryset, chapter_id=pk)
                if chapter:
                    serializer = ChapterSerializer(chapter)
                    return Response(serializer.data)
                else:
                    return Response(status.HTTP_404_NOT_FOUND)
            else:
                return Response(status.HTTP_403_FORBIDDEN)
        except:
            return Response(status.HTTP_500_INTERNAL_SERVER_ERROR)


    def partial_update(self, request, pk=None):
        try:
            if self.request.user.role == "Instructor" and self.request.user.is_verified:
                chapter = Chapter.objects.get(chapter_id=pk)
                serializer = ChapterSerializer(instance=chapter, data=request.data)
                
                if serializer.is_valid():
                    
                    serializer.save()
                    return Response(status.HTTP_200_OK)
                else:
                    return Response(status.HTTP_400_BAD_REQUEST)
            else:
                return Response(status.HTTP_403_FORBIDDEN)
        except:
            return Response(status.HTTP_500_INTERNAL_SERVER_ERROR)


    def destroy(self, request, pk=None):
        try:
            if self.request.user.role == "Instructor" and self.request.user.is_verified:
                queryset = Chapter.objects.filter(instructor=self.request.user.uid)
                chapter = get_object_or_404(queryset, chapter_id=pk)

                if chapter:
                    chapter.delete()
                    return Response(status.HTTP_200_OK)
                else:   
                    return Response(status.HTTP_404_NOT_FOUND)
            else:
                return Response(status.HTTP_403_FORBIDDEN)
        except:
            return Response(status.HTTP_500_INTERNAL_SERVER_ERROR)




class InstructorStudentsView(generics.ListAPIView):
    serializer_class = PurchasedCoursesSerializer
    permission_classes = [ IsAuthenticated ]


    def get_queryset(self):
        courses = UserCourse.objects.filter(course__instructor=self.request.user.uid)
        return courses




class InstructorStudentCourseView(generics.ListAPIView):
    serializer_class = StudentPurchasedCourseSerializer
    permission_classes = [ IsAuthenticated ]

    def get_queryset(self):
        instructor = self.request.user
        queryset = UserCourse.objects.filter(course__instructor=instructor).distinct("user_id")
        return queryset

