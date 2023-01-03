from django.urls import path

from . import views

urlpatterns = [
    path("", views.HomePageView.as_view(), name="home"),
    path("about/", views.AboutPageView.as_view(), name="about"),
    path("jobs/", views.JobIndexView.as_view(), name="job_index"),
    path("jobs/<int:pk>/", views.JobDetailView.as_view(), name="job_detail"),
    path("jobs/new/", views.JobCreateView.as_view(), name="job_create"),
    path("jobs/<int:pk>/edit/", views.JobUpdateView.as_view(), name="job_edit"),
    path("jobs/<int:pk>/delete/", views.JobDeleteView.as_view(), name="job_delete"),
    path("job_types/", views.JobTypeIndexView.as_view(), name="job_type_index"),
    path("job_types/<int:pk>/", views.JobTypeDetailView.as_view(), name="job_type_detail"),
    path("job_types/new/", views.JobTypeCreateView.as_view(), name="job_type_create"),
    path("job_types/<int:pk>/edit/", views.JobTypeUpdateView.as_view(), name="job_type_edit"),
    path("job_types/<int:pk>/delete/", views.JobTypeDeleteView.as_view(), name="job_type_delete"),
]
