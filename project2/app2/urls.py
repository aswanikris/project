from django.urls import path
from app2 import views

urlpatterns=[
    path('',views,fun)
    path("register", views.register_request, name="register")
]