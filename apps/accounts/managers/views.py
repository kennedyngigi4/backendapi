from django.shortcuts import render, get_object_or_404

from rest_framework import status, viewsets, generics, permissions
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from apps.accounts.models import *
from apps.accounts.serializers import *
from apps.accounts.permissions import *


class ManagerViewInstructors(viewsets.ViewSet):
    permission_classes = [ IsAuthenticated, IsManager ]


    def create(self, request):
        pass


    def list(self, request):
        try:
            queryset = User.objects.filter(role="Instructor")
            serializer = UserSerializer(queryset, many=True)
            
            return Response(serializer.data)
        except:
            return Response(status.HTTP_500_INTERNAL_SERVER_ERROR)


    def retrieve(self, request, pk=None):
        try:
            user = User.objects.get(uid=pk)
            serializer = InstructorSerializer(user)
            print(serializer.data)
            return Response(serializer.data)
        except:
            return Response(status.HTTP_500_INTERNAL_SERVER_ERROR)


    def partial_update(self, request, pk=None):
        pass


    def destroy(self, request, pk=None):
        pass




class ManagerViewStudents(viewsets.ViewSet):
    permission_classes = [ IsAuthenticated, IsManager ]

    def create(self, request):
        pass


    def list(self, request):
        try:
            queryset  = User.objects.filter(role="Student")
            serializer = UserSerializer(queryset, many=True)
            return Response(serializer.data)
        except:
            return Response(status.HTTP_500_INTERNAL_SERVER_ERROR)




