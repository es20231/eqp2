from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("tutorial4/", include("tutorial4.urls")),
    path('admin/', admin.site.urls)
]