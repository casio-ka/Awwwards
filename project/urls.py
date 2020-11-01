from django.urls import path,include
from django.contrib.auth.views import LogoutView
from .views import home

urlpatterns=[
    path('' ,home, name = 'welcome'),
]