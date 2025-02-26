from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/account/', include('apps.accounts.urls')),
    path('api/account/manager/', include('apps.accounts.managers.urls')),
    path('api/courses/manager/', include("apps.courses.managers.urls")),
    path('api/courses/instructor/', include('apps.courses.instructors.urls'),),
    
    path( 'api/courses/', include('apps.courses.urls')),
]


# URLS FOR COURSES
urlpatterns += [
    path('api/courses/student/', include("apps.courses.students.urls")),
]


# URLS FOR COMPETITIONS APP
urlpatterns += [
    path('api/competitions/manager/', include('apps.competitions.managers.urls')),
]


# URLS FOR PAYMENTS
urlpatterns += [
    path('api/payments/student/', include('apps.payments.urls')),
]


urlpatterns += static( settings.STATIC_URL, document_root=settings.STATIC_ROOT )
urlpatterns += static( settings.MEDIA_URL, document_root=settings.MEDIA_ROOT )



