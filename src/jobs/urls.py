from django.urls import path

from . import views

urlpatterns = [
     path('', views.HomePageView.as_view(), name='home'),
     path('about/', views.AboutPageView.as_view(), name='about'),
     path('jobs/', views.JobIndexView.as_view(), name='job_index'),
     path('jobs/<int:pk>/', views.JobDetailView.as_view(), name='job_detail'),
     path('jobs/create/', views.JobCreateView.as_view(), name='job_create'),
     path('jobs/<int:pk>/update/', views.JobUpdateView.as_view(), name='job_update'),
     path('jobs/<int:pk>/delete/', views.JobDeleteView.as_view(), name='job_delete'),
     path('job_types/', views.JobTypeIndexView.as_view(), name='job_type_index'),
     path('job_types/<int:pk>/', views.JobTypeDetailView.as_view(), name='job_type_detail'),
     path('job_types/create/', views.JobTypeCreateView.as_view(), name='job_type_create'),
     path('job_types/<int:pk>/update/', views.JobTypeUpdateView.as_view(), name='job_type_update'),
     path('job_types/<int:pk>/delete/', views.JobTypeDeleteView.as_view(), name='job_type_delete'),
     path('employees/', views.EmployeeIndexView.as_view(), name='employee_index'),
     path('employees/<int:pk>/', views.EmployeeDetailView.as_view(), name='employee_detail'),
     path('employees/create/', views.EmployeeCreateView.as_view(), name='employee_create'),
     path('employees/<int:pk>/update/', views.EmployeeUpdateView.as_view(), name='employee_update'),
     path('employees/<int:pk>/delete/', views.EmployeeDeleteView.as_view(), name='employee_delete'),
     path('worked_hours/', views.WorkedHoursIndexView.as_view(), name='worked_hours_index'),
     path('worked_hours/<int:pk>/', views.WorkedHoursDetailView.as_view(), name='worked_hours_detail'),
     
]
