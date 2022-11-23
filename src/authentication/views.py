from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import CreateView, UpdateView, DetailView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.


class LoginView(LoginView):
    template_name = 'authentication/login.html'
    next_page = reverse_lazy("home")


class LogoutView(LogoutView):
    template_name = 'authentication/logout.html'


class RegisterView(SuccessMessageMixin, CreateView):
    model = User
    template_name = 'authentication/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('login')
    success_message = "Account created successfully"

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return reverse_lazy('home')
        return super(RegisterView, self).get(*args, **kwargs)


class ProfileView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'authentication/profile.html'
    context_object_name = 'user'

    def get_object(self, queryset=None):
        return self.request.user


class UpdateProfileView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = User
    template_name = 'authentication/update_profile.html'
    fields = ['username', 'first_name', 'last_name', 'email']
    success_url = reverse_lazy('profile')
    success_message = "Profile updated successfully"

    def get_object(self, queryset=None):
        return self.request.user
