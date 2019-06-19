from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView as AuthLoginView
from django.contrib.auth import logout
from django.shortcuts import render
from django.contrib import messages

from .forms import CustomUserCreationForm

class SignUpView(SuccessMessageMixin, CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
    
    def get_success_message(self, cleaned_data):
        return "Your account has been succesfully created!"


class LoginView(SuccessMessageMixin, AuthLoginView):
    form_class = AuthenticationForm
    success_url = reverse_lazy('landing_page')
    template_name = 'registration/login.html'

    def get_success_message(self, cleaned_data):
        return "You have succesfully logged in!"


def logout_view(request):
    logout(request)
    messages.info(request, 'Succesfully logged out!')
    return render(request, 'landing_page.html')


