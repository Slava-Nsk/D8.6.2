from django.contrib import admin
from django.urls import path, include
from .views import UserInfoPage, make_author


urlpatterns = [
    path('', UserInfoPage.as_view(), name='info'),
    path('upgrade/', make_author, name = 'make_author')
]
