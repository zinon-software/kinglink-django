# rest framewoark
from .models import *
from .serializer import *
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework import generics


class GroubApi(generics.ListCreateAPIView):
    queryset = Groub.objects.order_by('-id')
    serializer_class = GroubSerializers

class GroubDetailApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Groub.objects.all()
    serializer_class = GroubSerializers
    lookup_field = 'id'


class CommentApi(generics.ListCreateAPIView):
    queryset = Comment.objects.order_by('-id')
    serializer_class = CommentSerializers

class CommentDetailApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializers
    lookup_field = 'id'