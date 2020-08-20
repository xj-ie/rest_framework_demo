import json

from django import http

from django.shortcuts import render

# Create your views here.
from django.views import View
# from requests import Response
from rest_framework.views import APIView, Response
from books.models import BookInfo

from books.serializers import Bookserializer

from books.serializers import BookValserializer


class Books(APIView):
    def get(self,request):
        print(request.query_params) #=>djaongo.views.View request.GET
        book = BookInfo.objects.all()
        res = Bookserializer(book, many=True)
        return Response(res.data)
    def post(self, request):
        # body = request.body.decode()
        # dict_str = json.loads(body)
        data = request.data # 相等于上面两行
        res = BookValserializer(data=data)
        res.is_valid()
        res.save()
        return Response(res.data)