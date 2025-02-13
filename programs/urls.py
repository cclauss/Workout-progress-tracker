from django.urls import path, re_path, include
from .views import WorkoutDayCreateView, WorkoutSessionCreateView
app_name="programs"

urlpatterns = [
    path("day/", WorkoutDayCreateView.as_view(), name="day"),
    path("session/", WorkoutSessionCreateView.as_view(),  name="session"),
]
