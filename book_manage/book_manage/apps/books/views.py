from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from books.models import BookInfo
from books.serializers import BookValserializer


class BooksDRF(ModelViewSet):
    queryset = BookInfo.objects.all()
    serializer_class = BookValserializer