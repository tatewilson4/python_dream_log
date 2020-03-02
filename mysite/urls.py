from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path('', include('dreams.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
]