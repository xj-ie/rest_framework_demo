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

class BookValserializer(serializers.Serializer):
    name = serializers.CharField(max_length=20,min_length=5)
    pub_date = serializers.DateField(required=False)
    readcount = serializers.IntegerField(max_value=100,min_value=5)
    commentcount = serializers.IntegerField(default=10)
    def validate_name(self,book_name):
        if book_name == 'python':
            raise serializers.ValidationError('书名不能是python')
        return book_name
    def validate(self,value):
        if value['readcount']>value['commentcount']:
            raise serializers.ValidationError('not readcount > commentcount')
        return value



