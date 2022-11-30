from django.contrib import admin
from django.urls import include, path

"""Assign the urls to each view"""
urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]