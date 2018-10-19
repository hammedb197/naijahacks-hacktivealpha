
from django.contrib import admin

from django.urls import include, path

urlpatterns = [
            path('phishchecker/', include('phish_checker.urls')),
            path('admin/', admin.site.urls),
        ]
