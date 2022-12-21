from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.UserLoginView.as_view(), name="user_login"),
    path("logout/", views.UserLogoutView.as_view(), name="user_logout"),
    path("register/", views.UserRegisterView.as_view(), name="user_register"),
    path("index/", views.UserIndexView.as_view(), name="user_index"),
    path("profile/<int:pk>/", views.UserProfileView.as_view(), name="user_profile"),
    path("update/<int:pk>/", views.UserUpdateView.as_view(), name="user_update"),
    path("delete/<int:pk>/", views.UserDeleteView.as_view(), name="user_delete"),

]
