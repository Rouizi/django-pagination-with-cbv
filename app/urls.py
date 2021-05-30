# app/urls.py
from django.contrib import admin
from django.urls import path

from core.views import ListUsers

urlpatterns = [
    path('admin/', admin.site.urls),
    path('list_users/', ListUsers.as_view(), name='list_users')
]