from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import Http404
from .models import Notification
from . tasks import send_email_task
from rest_framework import generics
from .serializers import NotificationSerializer, NotificationViewSet


def index(request):
    send_email_task.delay()
    return HttpResponse('<h1>EMAIL HAS BEEN SENT WITH CELERY!</h1>')


class NotificationList(generics.ListCreateAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer


class NotificationDetail(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = NotificationSerializer

    def get_object(self):
        obj = get_object_or_404(Notification, pk=self.kwargs.get('notification_id'))
        return obj
