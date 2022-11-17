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
    template_name = 'login.html'
    next_page = reverse_lazy("home")


class LogoutView(LogoutView):
    template_name = 'logout.html'


class RegisterView(SuccessMessageMixin, CreateView):
    model = User
    template_name = 'register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('login')
    success_message = "Account created successfully"

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return reverse_lazy('home')
        return super(RegisterView, self).get(*args, **kwargs)
