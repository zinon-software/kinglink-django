from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from account.models import Profile
from group.models import Group
from notification.models import Notification
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

        follows_users = Profile.objects.filter(user__in=follows_users)

        follows_posts = Group.objects.filter(created_by__in=follows_users)

        group_list = Group.objects.filter(created_by=user.profile)
        group_list = (follows_posts|group_list).distinct().order_by('-created_dt')

        # groups = Group.objects.filter(created_by = request.user.id)
        serializer = GroupSerializers(group_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def post(self, request, *args, **kwargs):

        data = {
            'titel': request.data.get('titel'), 
            'link': request.data.get('link'), 
            'created_by': request.user.profile.id,
            'category': request.data.get('category'), 
            'sections': request.data.get('sections'), 
        }

        serializer = PostGroupSerializers(data=data)
        if serializer.is_valid():
            data = serializer.save()


            # ارسال الاشعارات للمستخدمين بخصوص المنشور الجديد
            followers_users = request.user.profile.followers.all()
            followers_users = Profile.objects.filter(user__in=followers_users)
            for follower_user in followers_users:
                Notification.objects.create(sender=request.user.profile, receiver=follower_user, post=data, action= f"قام @{request.user.username} بالعجاب ب {data.titel}")
            
            
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
        group_instance = self.get_object(group_id, request.user.profile.id)
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
        group_instance = self.get_object(group_id, request.user.profile.id)
        if not group_instance:
            return Response(
                {"res": "المجموعة غير موجودة"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'titel': request.data.get('titel'), 
            'link': request.data.get('link'), 
            'created_by': request.user.profile.id,
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
        group_instance = self.get_object(group_id, request.user.profile.id)
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

class LikeApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, group_id):
        '''
        Helper method to get the object with given group_id, and user_id
        '''
        try:
            return Group.objects.get(id=group_id)
        except Group.DoesNotExist:
            return None

    def post(self, request, *args, **kwargs):
        user = request.user.profile
        pk = request.POST.get('pk', None)

        group_instance = self.get_object(pk)
        if not group_instance:
            return Response(
                {"res": "المجموعة غير موجودة"},
                status=status.HTTP_400_BAD_REQUEST
            )


        if group_instance.likes.filter(id=user.id).exists():
            group_instance.likes.remove(user)
            like = False
            post_id = '#like'+str(group_instance.id)
        else:
            group_instance.likes.add(user)
            like = True
            post_id = '#like'+str(group_instance.id)
            Notification.objects.create(sender=request.user.profile, receiver=group_instance.created_by, post=group_instance, action= f"قام @{request.user.username} بالعجاب ب {group_instance.titel}")
        
           
        data = {'likes_count': group_instance.total_likes,'like':like,'post_id':post_id}
        return Response(data, status=status.HTTP_200_OK)