from django.utils.translation import activate
from rest_framework.decorators import permission_classes
from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.response import Response
from dashboard.api.serializer import GroupReviewSerializers
from group.models import Group
from group.api.serializer import GroupSerializers
from notification.models import Notification


class GroupsReviewAPIView(APIView):
    permission_classes = [permissions.IsAdminUser]
    def get(self, request, *args, **kwargs):
        group_list = Group.objects.filter(activation=False)
        serializer = GroupSerializers(group_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    
    def get_object(self, group_id):

        try:
            return Group.objects.get(id=group_id, activation=False)
        except Group.DoesNotExist:
            return None
    
    def put(self, request, *args, **kwargs):

        group_instance = self.get_object(request.data.get('id'))

        if not group_instance:
            return Response(
                {"res": "المجموعة غير موجودة"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        group_instance.activation = True
        group_instance.save()

        Notification.objects.create(sender=request.user.profile, receiver=group_instance.created_by, post=group_instance, action= f"قام @{request.user.username} بنشر مجموعتك {group_instance.titel}")
        
        return Response("published ", status=status.HTTP_200_OK)


    def delete(self, request, group_id, *args, **kwargs):
        '''
        Deletes the todo item with given group_id if exists
        '''
        group_instance = self.get_object(request.data.get('id'))
        if not group_instance:
            return Response(
                {"res": "المجموعة غير موجودة"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        group_instance.delete()
        return Response(
            {"res": "تم حذف الكائن!"},
            status=status.HTTP_200_OK
        )

