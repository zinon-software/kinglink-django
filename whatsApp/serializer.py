# rest framewoark
### get data form model ---> json

from rest_framework import serializers
from .models import Groub

class GroubSerializers(serializers.ModelSerializer):
    class Meta:
        model = Groub
        fields = '__all__'
