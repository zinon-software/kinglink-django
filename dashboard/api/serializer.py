from rest_framework.serializers import Serializer
from dashboard.models import Sections
from rest_framework import serializers

from group.models import Group

class GroupReviewSerializers(Serializer):

    class Meta:
        model = Group
        fields = ["activation"] 

class SectionsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Sections
        fields = '__all__' 