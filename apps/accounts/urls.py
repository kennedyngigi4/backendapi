from django.urls import path
from apps.accounts.views import *
from rest_framework_simplejwt.views import ( TokenObtainPairView )
from rest_framework.routers import DefaultRouter

routers = DefaultRouter()
routers.register(r'profile', UserProfileView, basename='profile'),
urlpatterns = routers.urls

urlpatterns += [
    path( 'register/', RegistrationView.as_view(), name='register', ),
    path( 'login/', TokenObtainPairView.as_view(), name='login', ),
]

