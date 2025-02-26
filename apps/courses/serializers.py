from rest_framework import serializers
from apps.courses.models import *
from apps.accounts.serializers import UserSerializer


class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = [
            'chapter_id', 'course', 'title', 'description', 'videoUrl', 'position', 'is_published', 'is_free', 'videoPath', 'instructor'
        ]


class AttachmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Attachment
        fields = [
            'attachment_id', 'course', 'attached_file', 'chapter', 'created_at', 'created_by'
        ]


class CourseSerializer(serializers.ModelSerializer):
    chapters = ChapterSerializer(many=True, required=False)
    attachments = AttachmentSerializer(many=True, required=False)

    class Meta:
        model = Course
        fields = [
            'course_id', 'title', 'description', 'level', 'price', 'image', 'imagePath', 'preview_video', 'skills', 
            'is_published', 'manager', 'instructor', 'category', 'chapters', 'attachments', 'created_at', 'updated_at'
        ]



class UserCourseSerializer(serializers.ModelSerializer):
    course_title = serializers.SerializerMethodField()
    course_category = serializers.SerializerMethodField()

    class Meta:
        model = UserCourse
        fields = [
            'id', 'user_id', 'course', 'progress', 'is_complete', 'completed_at', 'certificate_url', 'certificatePath', 'enrolled_at', 'course_title', 'course_category'
        ]


    def get_course_title(self, obj):
        return obj.course.title


    def get_course_category(self, obj):
        return obj.course.category



class OnlineClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = OnlineClass
        fields = [
            "class_id", "title", "schedule", "course", "description", "created_at", "created_by"
        ]



