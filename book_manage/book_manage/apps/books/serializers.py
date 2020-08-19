from rest_framework import serializers

class Bookserializer(serializers.Serializer):
    name = serializers.CharField()
    pub_date = serializers.DateField()
    readcount = serializers.IntegerField()