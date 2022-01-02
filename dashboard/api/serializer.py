from rest_framework.serializers import Serializer
from dashboard.models import Sections

from group.models import Group

class GroupReviewSerializers(Serializer):

    class Meta:
        model = Group
        fields = ["activation"] 

class SectionsSerializers(Serializer):
    class Meta:
        model = Sections
        fields = '__all__' 