import json

from django import http

from django.shortcuts import render

# Create your views here.
from django.views import View
# from requests import Response
# from rest_framework.views import APIView, Response
from books.models import BookInfo
from rest_framework.generics import GenericAPIView
from rest_framework.views import Response
from rest_framework.mixins import ListModelMixin,RetrieveModelMixin,CreateModelMixin,DestroyModelMixin,UpdateModelMixin
from books.serializers import Bookserializer

from books.serializers import BookValserializer
# import sys
# sys.setrecursionlimit(100000)


class Books(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = BookInfo.objects.all()
    # ＃指定查询类视图数据
    # salizer_class = Bookserializer
    serializer_class = Bookserializer

    def get(self,request):
        return self.list(request)
    def post(self, request):
        # body = request.body.decode()
        # dict_str = json.loads(body)
        data = request.data # 相等于上面两行
        res = BookValserializer(data = data)
        res.is_valid()
        res.save()
        return Response(res.data)
class Books_update(GenericAPIView, UpdateModelMixin, DestroyModelMixin):
    queryset = BookInfo.objects.all()
    serializer_class = BookValserializer
    def put(self, request, pk):
        return self.update(request, pk)
    def delete(self, request, pk):
        return self.delete(request, pk)