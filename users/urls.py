from django.contrib import admin
from django.urls import path, include

from .views import SignUpView, LoginView, logout_view

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
]
