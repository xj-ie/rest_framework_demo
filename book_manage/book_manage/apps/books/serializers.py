from rest_framework import serializers

from books.models import BookInfo


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
    pub_date = serializers.DateField()
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

    def create(self, validated_data):
        books = BookInfo.objects.create(**validated_data)
        return books

    def update(self, instance, validated_data):
        instance.name = validated_data['name']
        instance.save()
        return instance


class BookModelSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=10) # 修改名称的最长度
    sms_vlid = serializers.CharField(min_length=5, max_length=5)

    # 添加未有的字段，但是必需在下面的字段中写入


    class Meta:
        model = BookInfo    # 指定根据db demo charset
        # fields = ('name', 'readcount')  #  rundatabase_class charset
        # fields = '__all__'  #create all database_class charset
        exclude = ('pub_date', ) # 排斥这个字符，其他的都写入   

        read_only_fields = ("commentcount", )# 添加一个read_only 属性
        extra_kwargs = {
            'readcount':{
                'default':10
            }
        }
        #oange gander char default count
        