# rest framewoark
### get data form model ---> json

from rest_framework import serializers
from .models import *

class GroubSerializers(serializers.ModelSerializer):
    class Meta:
        model = Groub
        fields = '__all__'
        depth = 1

class GroupPostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Groub
        fields = '__all__'

class CommentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class ReportSerializers(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class SectionsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Sections
        fields = '__all__'

