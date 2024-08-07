from django.urls import path
from app1.views import home1

urlpatterns=[
    path('',home1),
]