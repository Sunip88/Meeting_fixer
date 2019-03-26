
from django.urls import path, include

from .views import Home, StartMeetingView

urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("start-meeting/", StartMeetingView.as_view(), name="start-meeting"),
]