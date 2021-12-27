# rest framewoark
### get data form model ---> json

from rest_framework import serializers

from group.models import Group, Sections

class GroupSerializers(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'
        depth = 1

class PostGroupSerializers(serializers.ModelSerializer):
     class Meta:
        model = Group
        fields = ["titel", "link", "category", "sections", "created_by"] 

class SectionsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Sections
        fields = '__all__' 