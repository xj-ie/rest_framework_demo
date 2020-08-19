import json

from django import http

from django.shortcuts import render

# Create your views here.
from django.views import View

from books.models import BookInfo

from books.serializers import Bookserializer

from books.serializers import BookValserializer


class Books(View):
    def get(self,request):
        book = BookInfo.objects.all()
        res = Bookserializer(book,many=True)
        return http.JsonResponse(res.data, safe=False)
    def post(self, request):
        body = request.body.decode()
        dict_str = json.loads(body)
        res = BookValserializer(data=dict_str)
        res.is_valid()
        res.save()
        return http.JsonResponse(res.data)