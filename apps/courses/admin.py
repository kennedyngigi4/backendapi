from django.contrib import admin
from apps.courses.models import *
# Register your models here.

admin.site.register(Category)
admin.site.register(Course)
admin.site.register(Chapter)
admin.site.register(Attachment)
admin.site.register(UserCourse)

