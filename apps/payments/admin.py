from django.contrib import admin
from apps.payments.models import Payment, Purchase
# Register your models here.


admin.site.register(Payment)
admin.site.register(Purchase)


