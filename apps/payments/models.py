import uuid
from django.db import models

# Create your models here.



class Payment(models.Model):
    status_choices = [
        ('pending', 'pending', ),
        ('completed', 'completed', ),
        ('failed', 'failed', ),
        ('refunded', 'refunded', ),
    ]


    payment_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    user_id = models.CharField(max_length=255, null=True)
    course_id  = models.CharField(max_length=255, null=True)
    amount = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    currency  = models.CharField(max_length=15, default='USD', null=True)
    status = models.CharField(max_length=30, choices=status_choices, default=status_choices[1][0], null=True)
    transaction_id = models.CharField(max_length=255, null=True, unique=True)
    payment_method  = models.CharField(max_length=30, null=True)
    paid_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.payment_id)



class Purchase(models.Model):

    status_choices = [
        ('pending', 'pending', ),
        ('completed', 'completed', ),
        ('failed', 'failed', ),
        ('refunded', 'refunded', ),
    ]


    purchase_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    user_id = models.CharField(max_length=255, null=True, blank=True)
    course_id  = models.CharField(max_length=255, null=True, blank=True)
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE, null=True)
    amount = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    currency  = models.CharField(max_length=15, default='USD', null=True)
    status = models.CharField(max_length=30, null=True, blank=True)
    payment_method  = models.CharField(max_length=30, null=True, blank=True)
    purchased_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField(null=True, blank=True)


    def __str__(self):
        return str(self.purchase_id)
