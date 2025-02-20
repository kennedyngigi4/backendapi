import os

from django.shortcuts import render, get_object_or_404
from django.conf import settings
from rest_framework import generics, status, viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from apps.courses.models import *
from apps.courses.serializers import *
from apps.courses.students.certificate import *


class PurchasedCourses(generics.ListAPIView):
    permission_classes = [ IsAuthenticated ]
    serializer_class = UserCourseSerializer
    queryset = UserCourse.objects.all()

    def get_queryset(self):
        try:
            
            queryset = UserCourse.objects.filter(user_id=self.request.user.uid)
            serializer = UserCourseSerializer(queryset, many=True)
            return queryset
        except:
            return Response(status.HTTP_500_INTERNAL_SERVER_ERROR)
        


class PurchasedCourseDetails(generics.RetrieveAPIView):
    permission_classes = [ IsAuthenticated ]
    serializer_class = UserCourseSerializer
    queryset = UserCourse.objects.all()




class CourseDetails(generics.RetrieveAPIView):
    permission_classes = [ IsAuthenticated ]
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


class ChapterDetailsView(generics.RetrieveAPIView):
    permission_classes = [ IsAuthenticated ]
    serializer_class = ChapterSerializer
    queryset = Chapter.objects.all()



class ProgressUpdateView(generics.RetrieveUpdateAPIView):
    permission_classes = [ IsAuthenticated ]
    serializer_class = UserCourseSerializer
    queryset = UserCourse.objects.all()
    lookup_field = 'pk'
   

class CourseCompletionView(generics.RetrieveUpdateAPIView):
    permission_classes = [ IsAuthenticated ]
    serializer_class = UserCourseSerializer
    queryset = UserCourse.objects.all()


    def update(self, request, *args, **kwargs):
        inputPDF = os.path.join(settings.BASE_DIR, "certificates", "cert.pdf")
        
        storageFolder = os.path.join(settings.MEDIA_ROOT, f"users/{self.request.user.uid}/certificates/")
        os.makedirs(storageFolder, exist_ok=True)
        outPDF_path = os.path.join(storageFolder, "test.pdf")
        Certificate.generate_certificate(inputPDF, outPDF_path, self.request.user.fullname)
        kwargs['partial'] = True
        request.data["certificate_url"] = outPDF_path
        return super().update(request, *args, **kwargs)




