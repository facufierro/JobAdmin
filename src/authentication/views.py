from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView
from .forms import CustomUserCreationForm


class UserLoginView(LoginView):
    template_name = "authentication/user_login.html"
    next_page = reverse_lazy("home")


class UserLogoutView(LogoutView):
    template_name = "authentication/user_logout.html"
    next_page = reverse_lazy("home")


class UserRegisterView(SuccessMessageMixin, CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("user_login")
    template_name = "authentication/user_register.html"
    success_message = "Account created successfully"
