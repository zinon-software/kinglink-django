from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.response import Response
from notification.api.serializer import NotificationSerializers
from notification.models import Notification

class NotificationAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):

        notifications = Notification.objects.filter(receiver=request.user.id)
        notfy =NotificationSerializers(notifications, many=True)

        return Response(notfy.data, status=status.HTTP_200_OK)

class NotificationUpdateAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, *args, **kwargs):
        notifications = Notification.objects.filter(receiver=request.user.id)
        for notification in notifications.all():
            if notification.read == False:
                notification.read = True
                notification.save()
        return Response("مقروئات", status=status.HTTP_200_OK)