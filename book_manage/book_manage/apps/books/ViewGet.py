import json

from django import http

from django.shortcuts import render

# Create your views here.
from django.views import View
# from requests import Response
# from rest_framework.views import APIView, Response
from books.models import BookInfo
# from rest_framework.generics import GenericAPIView
from rest_framework.views import Response
# from rest_framework.mixins import ListModelMixin,RetrieveModelMixin,CreateModelMixin,DestroyModelMixin,UpdateModelMixin
from rest_framework.viewsets import ViewSet
from rest_framework.viewsets import GenericViewSet
from books.serializers import Bookserializer

from books.serializers import BookValserializer
# import sys
# sys.setrecursionlimit(100000)


class Books(ViewSet):
    # queryset = BookInfo.objects.all()
    # # ＃指定查询类视图数据
    # # salizer_class = Bookserializer
    # serializer_class = Bookserializer
    throttle_scope = "Books"
    filter_fields = ('btitle', 'bread')
    def list(self,request):
        # return self.list(request)
        data = BookInfo.objects.all()
        res = Bookserializer(data, many=True)
        return Response(res.data)
    def create(self, request):
        # body = request.body.decode()
        # dict_str = json.loads(body)
        data = request.data  # 相等于上面两行
        res = BookValserializer(data=data)
        res.is_valid()
        print(res.errors)
        res.save()
        return Response(res.data)
class Books_update(ViewSet):
    # queryset = BookInfo.objects.all()
    # serializer_class = BookValserializer
    def update(self, request, pk):
        data = request.data
        try:
            book = BookInfo.objects(id=pk)
        except Exception:
            return Response('Eroor')
        res = BookValserializer(book, data=data)
        res.is_valid()
        # is_valid
        res.save()
        return Response(res.data)
        # return self.update(request, pk)
    def delete(self, request, pk):
    #     book = BookInfo.objects
        try:
            book = BookInfo.objects.get(id=pk)
            book.is_delete=True
            book.save()
        except Exception:
            return Response('False')
        return Response('True')
