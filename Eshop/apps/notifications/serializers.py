from rest_framework import serializers, viewsets
from .models import Notification


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = [
            'notify_receiver',
            'notify_method',
            'notify_title',
            'notify_message',
            'notify_date',
        ]


class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
