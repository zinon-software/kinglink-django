# rest framewoark
### get data form model ---> json

from rest_framework import serializers
from .models import Groub, Comment

class GroubSerializers(serializers.ModelSerializer):
    class Meta:
        model = Groub
        fields = '__all__'

class CommentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'