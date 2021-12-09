from rest_framework import serializers

from comment.models import Comment

class CommentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        depth = 1


class PostCommentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
