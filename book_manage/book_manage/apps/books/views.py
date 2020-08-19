from django import http

from django.shortcuts import render

# Create your views here.
from django.views import View

from books.models import BookInfo

from books.serializers import Bookserializer


class Books(View):
    def get(self,request):
        book = BookInfo.objects.all()
        res = Bookserializer(book,many=True)
        return http.JsonResponse(res.data, safe=False)