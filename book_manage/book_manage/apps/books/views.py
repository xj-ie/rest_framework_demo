import json

from django import http

from django.shortcuts import render

# Create your views here.
from django.views import View
# from requests import Response
# from rest_framework.views import APIView, Response
from books.models import BookInfo
from rest_framework.generics import GenericAPIView
from rest_framework.views import  Response

from books.serializers import Bookserializer

from books.serializers import BookValserializer


class Books(GenericAPIView):
    queryset = BookInfo.objects.all()
    # ＃指定查询类视图数据
    # salizer_class = Bookserializer
    serializer_class = Bookserializer

    def get(self,request):

        # print(request.query_params) #=>djaongo.views.View request.GET
        book = self.get_queryset()  # 获取所有数据..      # self.get_objects()
        res = self.get_serializer(book, many=True)
        return Response(res.data)
    def post(self, request):
        # body = request.body.decode()
        # dict_str = json.loads(body)
        data = request.data # 相等于上面两行
        res = BookValserializer(data = data)
        res.is_valid()
        res.save()
        return Response(res.data)
class Books_update(GenericAPIView):
    queryset = BookInfo.objects.all()
    serializer_class = BookValserializer
    def put(self, request, pk):
        data = request.data
        try:
            book = self.get_object()
        except Exception:
            return http.HttpResponseForbidden('NON')
        ser = self.get_serializer(book,data=data)
        ser.is_valid()
        ser.save()
        return Response(ser.data)