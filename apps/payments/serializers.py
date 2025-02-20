
from rest_framework import serializers
from apps.payments.models import *



class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = [
            'payment_id', 'user_id', 'course_id', 'amount', 'status', 'payment_method', 'transaction_id', 'paid_at'
        ]



class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = [
            'user_id', 'course_id', 'amount', 'payment', 'currency', 'status', 'payment_method', 'purchased_at', 'expires_at'
        ]

