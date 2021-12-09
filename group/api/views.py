from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from group.models import Group
from .serializer import GroupSerializers, PostGroupSerializers

# Create your views here.

class MyGroupListApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        '''
        List all the group items for given requested user
        '''
        user = request.user

        follows_users = user.profile.follows.all()
        follows_posts = Group.objects.filter(created_by_id__in=follows_users)
        user_posts = Group.objects.filter(created_by=user)
        group_list = (follows_posts|user_posts).distinct().order_by('-created_dt')

        # groups = Group.objects.filter(created_by = request.user.id)
        serializer = GroupSerializers(group_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def post(self, request, *args, **kwargs):

        data = {
            'titel': request.data.get('titel'), 
            'link': request.data.get('link'), 
            'created_by': request.user.id,
            'category': request.data.get('category'), 
            'sections': request.data.get('sections'), 
        }

        serializer = PostGroupSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GroupDetailApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, group_id, user_id):
        '''
        Helper method to get the object with given group_id, and user_id
        '''
        try:
            return Group.objects.get(id=group_id, created_by=user_id)
        except Group.DoesNotExist:
            return None

    # 3. Retrieve
    def get(self, request, group_id, *args, **kwargs):
        '''
        Retrieves the Todo with given group_id
        '''
        group_instance = self.get_object(group_id, request.user.id)
        if not group_instance:
            return Response(
                {"res": "المجموعة غير موجودة"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        session_key = 'view_topic_{}'.format(group_id)
        if not request.session.get(session_key, False):
            group_instance.views += 1
            group_instance.save()
            request.session[session_key] = True

        serializer = GroupSerializers(group_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 4. Update
    def put(self, request, group_id, *args, **kwargs):
        '''
        Updates the todo item with given group_id if exists
        '''
        group_instance = self.get_object(group_id, request.user.id)
        if not group_instance:
            return Response(
                {"res": "المجموعة غير موجودة"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'titel': request.data.get('titel'), 
            'link': request.data.get('link'), 
            'created_by': request.user.id,
            'category': request.data.get('category'), 
            'sections': request.data.get('sections'), 
        }
        serializer = PostGroupSerializers(instance = group_instance, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 5. Delete
    def delete(self, request, group_id, *args, **kwargs):
        '''
        Deletes the todo item with given group_id if exists
        '''
        group_instance = self.get_object(group_id, request.user.id)
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

class UpdateViewsGroupApiView(APIView):
    permission_classes = [permissions.AllowAny]

    def get_object(self, group_id):
        '''
        Helper method to get the object with given group_id, and user_id
        '''
        try:
            return Group.objects.get(id=group_id)
        except Group.DoesNotExist:
            return None

    def get(self, request, group_id, *args, **kwargs):

        group_instance = self.get_object(group_id)
        if not group_instance:
            return Response(
                {"res": "المجموعة غير موجودة"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        session_key = 'view_group_{}'.format(group_id)
        if not request.session.get(session_key, False):
            group_instance.views += 1
            group_instance.save()
            request.session[session_key] = True

        serializer = GroupSerializers(group_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)