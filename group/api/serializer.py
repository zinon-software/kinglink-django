# rest framewoark
### get data form model ---> json

from django.db.models import fields
from rest_framework import serializers
from whatsApp.models import *

class MyGroubSerializers(serializers.ModelSerializer):
    class Meta:
        model = Groub
        fields = '__all__'
        depth = 1

class PostGroubSerializers(serializers.ModelSerializer):
     class Meta:
        model = Groub
        fields = ["name", "link", "category", "sections", "created_by"] 