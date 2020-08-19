from rest_framework import serializers
class PeopleInfoSerializer(serializers.Serializer):
    name = serializers.CharField()
    description = serializers.CharField()



class Bookserializer(serializers.Serializer):
    name = serializers.CharField()
    pub_date = serializers.DateField()
    readcount = serializers.IntegerField()
    # peopleinfo_set = serializers.PrimaryKeyRelatedField(read_only=True, many=True)
    # peopleinfo_set = serializers.StringRelatedField(read_only=True, many=True)
    peopleinfo_set = PeopleInfoSerializer(many=True)

