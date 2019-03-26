from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView

from .models import Meeting


class Home(View):
    def get(self, request):
        return render(request, 'meetings/main.html')


class StartMeetingView(CreateView):
    model = Meeting
    template_name = 'meetings/start_meeting.html'
    fields = '__all__'
