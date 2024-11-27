from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', include('tasks.urls')),
    path('accounts/', include('accounts.urls')),

    path('', lambda request: redirect('accounts:login'))
]
