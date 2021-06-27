# rest framewoark
from .models import *
from .serializer import *
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework import generics


class GroubApi(generics.ListCreateAPIView):
    queryset = Groub.objects.order_by('created_dt')
    serializer_class = GroubSerializers

class GroubDetailApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Groub.objects.all()
    serializer_class = GroubSerializers
    lookup_field = 'id'