from rest_framework.serializers import Serializer

from group.models import Group

class GroupReviewSerializers(Serializer):

    class Meta:
        model = Group
        fields = ["activation"] 
