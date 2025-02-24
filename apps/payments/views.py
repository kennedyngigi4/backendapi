from django.shortcuts import render, get_object_or_404

from rest_framework import generics, viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from apps.courses.models import UserCourse
from apps.payments.models import *
from apps.payments.serializers import *

# Create your views here.



class StudentPaymentView(generics.CreateAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()


    def create(self, request, *args, **kwargs):
        try:
            purchaseExists = UserCourse.objects.filter(course=request.data['course_id'], user_id=request.data['user_id']).exists()
            if purchaseExists:
                return Response(status.HTTP_409_CONFLICT)
            else:
                serializer = PaymentSerializer(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(status.HTTP_201_CREATED)
                else:
                    return Response(status.HTTP_406_NOT_ACCEPTABLE)
        except:
            return Response(status.HTTP_500_INTERNAL_SERVER_ERROR)



class StudentPurchasesListView(generics.ListAPIView):
    permission_classes = [ IsAuthenticated ]
    serializer_class = PurchaseSerializer
    queryset = Purchase.objects.all()

    def get_queryset(self):
        try:
            queryset = Purchase.objects.filter(user_id=self.request.user.uid)
            serializer = PurchaseSerializer(queryset, many=True)
            return Response(serializer.data)
        except:
            return Response(status.HTTP_500_INTERNAL_SERVER_ERROR)



class StudentPurchaseDetailsView(generics.RetrieveAPIView):
    permission_classes = [ IsAuthenticated ]
    serializer_class = PurchaseSerializer
    queryset = Purchase.objects.all()


    
