from django.urls import path
from apps.payments.views import *

urlpatterns = [
    path( 'payment', StudentPaymentView.as_view(), name='payment', ),
    path( 'purchases', StudentPurchasesListView.as_view(), name='purchases', ),
    path( 'purchase_details/<str:pk>', StudentPurchaseDetailsView.as_view(), name='purchase_details', ),
]

