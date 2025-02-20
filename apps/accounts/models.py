import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
# Create your models here.



class UserManager(BaseUserManager):
    def create_user(self, email, fullname, phone, gender, role, password=None):
        if not email:
            raise ValueError('Email is required')
        
        user = self.model(
            email=self.normalize_email(email).lower(),
            fullname=fullname,
            phone=phone,
            gender=gender,
            role=role,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    

    def create_admin(self, email, fullname, phone, gender, role, password=None):
        if not email:
            raise ValueError('Email is required')
        
        user = self.create_user(
            email=self.normalize_email(email).lower(),
            fullname=fullname,
            phone=phone,
            gender=gender,
            role=role,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, fullname, phone, gender, role, password=None):
        if not email:
            raise ValueError('Email is required')
        
        user = self.create_user(
            email=self.normalize_email(email).lower(),
            fullname=fullname,
            phone=phone,
            gender=gender,
            role=role,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user



def userFolder(instance, filename):
    return f"users/{instance.uid}/{filename}"


class User(AbstractBaseUser, PermissionsMixin):

    roles = [
        ( 'Student', 'Student', ),
        ( 'Parent', 'Parent', ),
        ( 'Instructor', 'Instructor', ),
        ( 'Trustee', 'Trustee', ),
        ( 'Admin', 'Admin', ),
    ]

    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    email = models.EmailField(unique=True)
    fullname = models.CharField(max_length=255, null=True)
    phone = models.CharField(max_length=20, null=True)
    gender = models.CharField(max_length=10, null=True)
    age_range = models.CharField(max_length=40, null=True)
    role = models.CharField(max_length=30, null=True, )
    profile_image = models.ImageField(upload_to=userFolder, null=True)

    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(null=True, blank=True)

    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'fullname', 'phone', 'gender', 'role'
    ]

    def __str__(self):
        return self.email





