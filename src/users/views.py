from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CustomUserCreationForm

from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import custom_user


class UserLoginView(LoginView):
    template_name = "users/user_login.html"
    next_page = reverse_lazy("home")


class UserLogoutView(LogoutView):
    template_name = "users/user_logout.html"
    next_page = reverse_lazy("home")


class UserRegisterView(SuccessMessageMixin, CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("user_index")
    template_name = "users/user_register.html"
    success_message = "Account created successfully"


# make a class based view for the list of users only visible to admins
class UserIndexView(ListView, LoginRequiredMixin):
    model = custom_user
    template_name = "users/user_index.html"
    context_object_name = "users"


class UserProfileView(DetailView, LoginRequiredMixin):
    model = custom_user
    template_name = "users/user_profile.html"
    context_object_name = "user"


class UserUpdateView(UpdateView, LoginRequiredMixin):
    model = custom_user
    template_name = "users/user_update.html"
    fields = ["email", "first_name", "last_name"]
    success_url = reverse_lazy("user_index")


class UserDeleteView(DeleteView, LoginRequiredMixin):
    model = custom_user
    template_name = "users/user_delete.html"
    success_url = reverse_lazy("user_index")
