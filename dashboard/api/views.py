from django.utils.translation import activate
from rest_framework.decorators import permission_classes
from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.response import Response
from dashboard.api.serializer import GroupReviewSerializers, SectionsSerializers
from dashboard.models import Sections
from group.models import Group
from group.api.serializer import GroupSerializers
from notification.models import Notification

class GroupsReviewAPIView(APIView):
    permission_classes = [permissions.IsAdminUser]
    def get(self, request, *args, **kwargs):
        group_list = Group.objects.filter(activation=False)
        serializer = GroupSerializers(group_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class GroupDetailReviewAPIView(APIView):
    permission_classes = [permissions.IsAdminUser]
    
    
    def get_object(self, group_id):

        try:
            return Group.objects.get(id=group_id, activation=False)
        except Group.DoesNotExist:
            return None
    
    def get(self, request, groupID, *args, **kwargs):
        group_instance = self.get_object(groupID)
        if not group_instance:
            return Response(
                {"res": "المجموعة غير موجودة"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        session_key = 'view_topic_{}'.format(groupID)
        if not request.session.get(session_key, False):
            group_instance.views += 1
            group_instance.save()
            request.session[session_key] = True

        serializer = GroupSerializers(group_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)


    
    def put(self, request,  groupID, *args, **kwargs):

        group_instance = self.get_object(groupID)

        if not group_instance:
            return Response(
                {"res": "المجموعة غير موجودة"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        group_instance.activation = True
        group_instance.save()

        if group_instance.activation == True:
            profile = group_instance.created_by
            profile.posts += 1
            profile.save()

        Notification.objects.create(sender=request.user.profile, receiver=group_instance.created_by, post=group_instance, action= f"قام @{request.user.username} بنشر مجموعتك {group_instance.titel}")
        
        return Response("published ", status=status.HTTP_200_OK)


    def delete(self, request, groupID, *args, **kwargs):
        '''
        Deletes the todo item with given group_id if exists
        '''
        group_instance = self.get_object(groupID)
        if not group_instance:
            return Response(
                {"res": "المجموعة غير موجودة"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        if group_instance.activation == True:
            profile = group_instance.created_by
            profile.posts -= 1
            profile.save()

        group_instance.delete()
        return Response(
            {"res": "تم حذف الكائن!"},
            status=status.HTTP_200_OK
        )



class SectionsAIPView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        sections = Sections.objects.all()

        serializer = SectionsSerializers(sections, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


