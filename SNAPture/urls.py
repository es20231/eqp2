from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include("dashboard.urls")),
    path("autenticacao/", include("autenticacao.urls")),
    path('admin/', admin.site.urls)
]
