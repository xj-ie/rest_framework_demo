from django.conf import settings
# from rest_framework import settings
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from books.models import BookInfo
from books.serializers import BookValserializer
from books.serializers import Bookserializer


class BooksDRF(ModelViewSet):
    queryset = BookInfo.objects.all()
    authentication_classes = (BasicAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated, )
    throttle_scope = 'BooksDRF'
    filter_fields = ('btitle', 'bread')

    def get_serializer_class(self):  #可以通过 这个来指定多个序列 化器
        if self.action in settings.SERIALIZERCHANGE_URL.values(): #通过这个来区别 类型来指定序列化器
            return BookValserializer
        else:
            return Bookserializer




    @action(methods=['get'], detail=True)
    def lastdata(self, request, pk):
        book = BookInfo.objects.get(id=pk)
        ser = BookValserializer(book)
        return Response(ser.data)