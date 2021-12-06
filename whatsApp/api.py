# rest framewoark
from .models import *
from .serializer import *
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework import generics

from django_filters.rest_framework import DjangoFilterBackend

# الروابط
class GroubApi(generics.ListCreateAPIView):
    permission_classes = []
    queryset = Groub.objects.filter(activation=True).order_by('-id')
    serializer_class = GroubSerializers
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['sections']

class GroupPostApi(generics.ListCreateAPIView):
    permission_classes = []
    queryset = Groub.objects.all()[:1]
    serializer_class = GroupPostSerializers

class GroubTopApi(generics.ListCreateAPIView):
    permission_classes = []
    queryset = Groub.objects.all().order_by('-views')[:18]
    serializer_class = GroubSerializers
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['sections']

class GroubDetailApi(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = []
    queryset = Groub.objects.all()
    serializer_class = GroubSerializers
    lookup_field = 'id'


# التعليقات
class CommentApi(generics.ListCreateAPIView):
    permission_classes = []
    queryset = Comment.objects.all()
    serializer_class = CommentSerializers
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['group']

class CommentDetailApi(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = []
    queryset = Comment.objects.all()
    serializer_class = CommentSerializers
    lookup_field = 'id'


# البلاغات
class ReportApi(generics.ListCreateAPIView):
    permission_classes = []
    queryset = Report.objects.all()
    serializer_class = ReportSerializers

class ReportDetailApi(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = []
    queryset = Report.objects.all()
    serializer_class = ReportSerializers
    lookup_field = 'id'


# الفئات
class CategoryApi(generics.ListCreateAPIView):
    permission_classes = []
    queryset = Category.objects.all()
    serializer_class = CategorySerializers

class CategoryDetailApi(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = []
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
    lookup_field = 'id'



# الاقسام
class SectionsApi(generics.ListCreateAPIView):
    permission_classes = []
    queryset = Sections.objects.all()
    serializer_class = SectionsSerializers

class SectionsDetailApi(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = []
    queryset = Sections.objects.all()
    serializer_class = SectionsSerializers
    lookup_field = 'id'
