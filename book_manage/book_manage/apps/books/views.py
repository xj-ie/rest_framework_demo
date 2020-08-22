from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from books.models import BookInfo
from books.serializers import BookValserializer


class BooksDRF(ModelViewSet):
    queryset = BookInfo.objects.all()
    serializer_class = BookValserializer
    @action(methods=['get'], detail=True)
    def lastdata(self, request, pk):
        book = BookInfo.objects.get(id=pk)
        ser = BookValserializer(book)
        return Response(ser.data)