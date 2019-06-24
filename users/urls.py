from django.contrib import admin
from django.urls import path, include

from .views import SignUpView, LoginView, logout_view, rate_me_login

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('login/rateme', rate_me_login, name='rate_me_login'),
    path('logout/', logout_view, name='logout'),
]
