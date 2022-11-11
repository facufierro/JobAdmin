from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from jobmanager import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
]
