from rest_framework import permissions, response, status
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from comment.api.serializers import PostCommentSerializers, CommentSerializers
from comment.models import Comment



class CommentListAPIView(APIView):

    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]

    def get(self, request, post_id, *args, **kwargs):

        comments = Comment.objects.filter(group=post_id)

        serializer = CommentSerializers(comments, many=True)
        return response.Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, post_id, *args, **kwargs):

        data = {
            "sender" : request.user.id,
            "group" : post_id,
            "message" : request.data.get('message'),
        }

        serializer = PostCommentSerializers(data=data)

        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_200_OK)
        
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PUTAndDeleteCommentAPIView(APIView):

    permission_classes = [permissions.IsAuthenticated,]

    def get_opject(self, comment_id, user_id):
        try:
            return Comment.objects.get(id=comment_id, sender=user_id)
        except:
            return None

    def put(self, request, comment_id, *args, **kwargs):
        comment_instance = self.get_opject(comment_id, request.user.id)

        if not comment_instance:
            return response.Response({"res": "المجموعة غير موجودة"}, 
                status=status.HTTP_400_BAD_REQUEST)
        
        data = {
            "sender" : request.user.id,
            "group" : comment_id,
            "message" : request.data.get('message'),
        }
        serializer = PostCommentSerializers(instance=comment_instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_200_OK)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, comment_id, *args, **kwargs):

        comment_instance = self.get_opject(comment_id, request.user.id)

        if not comment_instance:
            return response.Response({"res": "المجموعة غير موجودة"}, 
                status=status.HTTP_400_BAD_REQUEST)
        
        comment_instance.delete()

        return response.Response(
            {"res": "تم حذف الكائن!"},
            status=status.HTTP_200_OK
        )