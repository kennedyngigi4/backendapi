from django.shortcuts import render, get_object_or_404
from rest_framework import status, generics, viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


from apps.competitions.models import *
from apps.competitions.serializers import *


class ManagerBadgeView(viewsets.ViewSet):
    def create(self, request):
        try:
            serializer = BadgeSerializer(data=request.data)
            print(request.data)
            if serializer.is_valid():
                serializer.save(created_by=self.request.user.uid)
                return Response(status.HTTP_201_CREATED)
            else:
                return Response(status.HTTP_406_NOT_ACCEPTABLE)
        except:
            return Response(status.HTTP_500_INTERNAL_SERVER_ERROR)


    def list(self, request):
        try:
            queryset = Badge.objects.all()
            serializer = BadgeSerializer(queryset, many=True)
            return Response(serializer.data)
        except:
            return Response(status.HTTP_500_INTERNAL_SERVER_ERROR)


    def destroy(self, request, pk=None):
        try:
            queryset = Badge.objects.all()
            badge = get_object_or_404(queryset, badge_id=pk)

            if badge:
                badge.delete()
                return Response(status.HTTP_200_OK)
            else:
                return Response(status.HTTP_404_NOT_FOUND)

        except:
            return Response(status.HTTP_500_INTERNAL_SERVER_ERROR)

