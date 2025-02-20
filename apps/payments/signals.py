from django.dispatch import receiver
from django.db.models.signals import post_save
from rest_framework.response import Response
from apps.payments.models import Payment, Purchase
from apps.courses.models import UserCourse, Course


@receiver(post_save, sender=Payment)
def purchase_signal_receiver(sender, created, instance=None, *args, **kwargs):
    if created:
        try: 
            purchase = Purchase.objects.create(
                user_id=instance.user_id,
                course_id=instance.course_id,
                payment=instance,
                amount=instance.amount,
                currency=instance.currency,
                status=instance.status,
                payment_method=instance.payment_method,
            )

            purchase.save()
            return purchase
        except:
            return Response("Purchase rignal receiver failed")



@receiver(post_save, sender=Purchase)
def userCourse_signal_receiver(sender, created, instance=None, *args, **kwargs):
    if created:
        try:
            purchased_course = Course.objects.get(course_id=instance.course_id)
            user_course = UserCourse.objects.create(
                user_id=instance.user_id,
                course=purchased_course,
                purchase_id=instance.purchase_id,
            )
            print('Course adding ...')
            user_course.save()
            
            return user_course
        except:
            return Response("userCourse signal receiver failed")




