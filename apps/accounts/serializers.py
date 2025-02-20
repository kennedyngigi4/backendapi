from rest_framework import serializers
from apps.accounts.models import User
from apps.courses.models import Course, Chapter

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        extra_kwargs = { 'write_only': { 'password': True } }
        fields = [
            'email', 'fullname', 'phone', 'gender', 'role', 'password'
        ]


    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            fullname=validated_data['fullname'],
            phone=validated_data['phone'],
            gender=validated_data['gender'],
            role=validated_data['role'],
            password=validated_data['password'],
        )

        return user
    


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'uid','email', 'fullname', 'phone', 'gender', 'role', 'is_verified', 'profile_image', 'date_joined', 'last_login', 'age_range'
        ]



class InstructorSerializer(serializers.ModelSerializer):
    courses = serializers.SerializerMethodField()
    chapters = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            'uid','email', 'fullname', 'phone', 'gender', 'role', 'is_verified', 'profile_image', 'date_joined', 'last_login', 'courses', 'chapters'
        ]


    def get_courses(self, obj):
        return Course.objects.using("courses").filter(instructor=obj.uid).values('course_id','title', 'price', 'level', 'description')


    def get_chapters(self, obj):
        return Chapter.objects.using("courses").filter(instructor=obj.uid).values('chapter_id', 'title', 'description', 'is_free')



