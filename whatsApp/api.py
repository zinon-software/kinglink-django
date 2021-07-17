# rest framewoark
from .models import *
from .serializer import *
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework import generics


class GroubApi(generics.ListCreateAPIView):
    queryset = Groub.objects.filter(activation=True).order_by('-id')
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

class ReportApi(generics.ListCreateAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializers

class ReportDetailApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializers
    lookup_field = 'id'



class CategoryApi(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers

class CategoryDetailApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
    lookup_field = 'id'

class SectionsApi(generics.ListCreateAPIView):
    queryset = Sections.objects.all()
    serializer_class = SectionsSerializers

class SectionsDetailApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sections.objects.all()
    serializer_class = SectionsSerializers
    lookup_field = 'id'