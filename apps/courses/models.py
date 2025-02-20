import uuid
from django.db import models

# Create your models here.


class Category(models.Model):
    category_id = models.UUIDField(primary_key=True, editable=False, unique=True, default=uuid.uuid4)
    name  = models.CharField(max_length=255, null=True)

    def __str__(self) -> str:
        return self.name


def image_path(instance, filename):
        return f"courses/{instance.course_id}/{filename}"  


class Course(models.Model):
    course_id = models.UUIDField(primary_key=True, editable=False, unique=True, default=uuid.uuid4)
    title = models.CharField(max_length=255, null=True)
    description = models.TextField(null=True, blank=True)
    level = models.CharField(max_length=255, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    image = models.ImageField(upload_to=image_path, null=True, blank=True)
    preview_video = models.FileField(upload_to=image_path,  null=True, blank=True)
    skills = models.TextField(null=True, blank=True)
    is_published = models.BooleanField(default=False)
    instructor = models.CharField(max_length=255, null=True, blank=True)
    manager = models.CharField(max_length=255, null=True)
    category = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def imagePath(self):
        if not self.image:
            return None
        else:
            return f"http://127.0.0.1:8000/media/{self.image}" 
        
    def previewVideoURL(self):
        if not self.preview_video:
            return None
        else:
            return f"http://127.0.0.1:8000/{self.preview_video}"
        

    def __str__(self):
        return str(self.title)
    


def videoFolderPath(instance, filename):
    return f"courses/{instance.course.course_id}/chapter_videos/{filename}"

class Chapter(models.Model):
    chapter_id = models.UUIDField(primary_key=True, editable=False, unique=True, default=uuid.uuid4)
    course = models.ForeignKey(Course, related_name="chapters", on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=255, null=True)
    description = models.TextField(null=True, blank=True)
    videoUrl = models.FileField(upload_to=videoFolderPath, null=True, blank=True)
    position = models.IntegerField(default=1)
    is_published = models.BooleanField(default=False)
    is_free = models.BooleanField(default=False)
    instructor = models.CharField(max_length=255, null=True, blank=True)
    manager  = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)


    def videoPath(self):
        if not self.videoUrl:
            return None
        else:
            return f"http://127.0.0.1:8000/{self.videoUrl.url}" 

    def __str__(self):
        return str(self.title)


def AttachmentPath(instance, filename):
        return f"courses/{instance.course_id}/attachments/{filename}" 

class Attachment(models.Model):
    attachment_id = models.UUIDField(primary_key=True, editable=False, unique=True, default=uuid.uuid4)
    course = models.ForeignKey(Course, related_name='attachments', on_delete=models.CASCADE, null=True)
    attached_file = models.FileField(upload_to=AttachmentPath, null=True)
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.course.title
    


class Quiz(models.Model):
    quiz_id = models.UUIDField(primary_key=True, editable=False, unique=True, default=uuid.uuid4)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=255, null=True)
    description = models.TextField(null=True, blank=True)
    points = models.CharField(max_length=100, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f"{self.name} {self.course.title}"
    



class UserCourse(models.Model):

    id = models.UUIDField(primary_key=True, editable=False, unique=True, default=uuid.uuid4)
    user_id = models.CharField(max_length=255, null=True)
    course = models.ForeignKey(Course, related_name='courses', on_delete=models.CASCADE, null=True)
    purchase_id = models.CharField(max_length=255, null=True, unique=True)
    access_type = models.CharField(max_length=30, default='Lifetime')
    progress = models.IntegerField(null=True, default=0)
    is_complete = models.BooleanField(default=False) 
    completed_at = models.DateTimeField(null=True, blank=True)
    certificate_url = models.CharField(max_length=255, null=True, blank=True)
    enrolled_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)



