# rest framewoark
### get data form model ---> json

from rest_framework import serializers

from group.models import Group

class GroupSerializers(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'
        depth = 1

class PostGroupSerializers(serializers.ModelSerializer):
     class Meta:
        model = Group
        fields = ["name", "link", "category", "sections", "created_by"] 