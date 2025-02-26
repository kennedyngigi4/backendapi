from rest_framework import serializers
from apps.courses.models import *
from django.db import connections


class PurchasedCoursesSerializer(serializers.ModelSerializer):
    user_details = serializers.SerializerMethodField()
    course_name = serializers.SerializerMethodField()

    class Meta:
        model = UserCourse
        fields = "__all__"


    def get_course_name(self, obj):
        return obj.course.title

    def get_user_details(self, obj):
        user_id = obj.user_id

        with connections["accounts"].cursor() as cursor:
            cursor.execute("SELECT fullname FROM accounts_user WHERE uid= %s", [user_id])
            
            row = cursor.fetchone()

        return row[0] if row else None





class StudentPurchasedCourseSerializer(serializers.ModelSerializer):
    student_details = serializers.SerializerMethodField()
    courses = serializers.SerializerMethodField()

    class Meta:
        model = UserCourse
        fields = [
            "user_id","courses", "student_details"
        ]


    def get_student_details(self, obj):
        user_id = obj.user_id
        with connections["accounts"].cursor() as cursor:
            cursor.execute("SELECT fullname, email, phone FROM accounts_user WHERE uid=%s", [user_id])
            row = cursor.fetchone()
        return { "fullname": row[0], "email": row[1], "phone": row[2] } if row else None



    def get_courses(self, obj):
        instructor = self.context["request"].user
        enrolled_courses = UserCourse.objects.filter(user_id=obj.user_id, course__instructor=instructor)
        return enrolled_courses


